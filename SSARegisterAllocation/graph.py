from lang import Inst, Add, Mul, Lth, Geq, Bt, Phi, Env, interp
from dataflow import abstract_interp, liveness_constraint_gen
from collections import defaultdict


class MCSGraph:
    def __init__(s, program: list[Inst]):
        liveness = abstract_interp(liveness_constraint_gen(program))
        s.graph = defaultdict(lambda: set())
        s.weights = defaultdict(lambda: 0)
        s.maxweight = 0
        # build intersection graph
        for values in liveness.values():
            for var in values:
                s.V[var] |= set(values)
        s.weightedVs = sorted(s.weights.keys(), key=lambda x: s.weights[x])

    def N(s, v: str) -> set[str]:
        return s.graph[v]

    def update(s, v):
        for n in s.graph[v]:
            s.weights[n] += 1
        s.weightedVs = sorted(s.weights.keys(), key=lambda x: s.weights[x])

    def pop(s):
        pop = s.weightedVs.pop(0)
        del s.graph[pop]
        del s.weights[pop]
        for k, v in s.graph.items():
            s.graph[k].remove(pop)
        return pop

    def size(s):
        return len(s.graph)


def MaximumCardinalitySearch(program: list[Inst]):
    """
    TODO: add descricao de phi aqui

        >>> env = Env({
        ... 'result0': 0,
        ... 'zero': 0, 'one': 1, 'minone': -1,
        ... 'n0': 14, 'd': 5
        ... })
        >>> i0 = Lth('z', 'n0', 'd')
        >>> i2 = Mul('negd', 'd', 'minone')
        >>> i3 = Phi('result1', 'result0', 'result2')
        >>> i4 = Phi('n1', 'n0', 'n2')
        >>> i5 = Add('result2', 'result1', 'one')
        >>> i6 = Add('n2', 'n1', 'negd')
        >>> i7 = Geq('l', 'n2', 'd')
        >>> i9 = Add('remainder', 'zero', 'n2')
        >>> i10 = Add('end', 'zero', 'zero')
        >>> i1 = Bt('z', i10)
        >>> i8 = Bt('l', i3)
        >>> prog = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
        >>> for i in range(9):
        ...     prog[i].add_next(prog[i+1])
        >>> eqs = liveness_constraint_gen(prog)
        >>> liveness = abstract_interp(eqs)
        >>> liveness
    """
    g = MCSGraph(program)
    sequence = list()
    for i in range(g.size()):
        sequence.append(g.pop())
    return sequence
