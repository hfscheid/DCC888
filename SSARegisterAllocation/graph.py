from lang import Inst, Add, Mul, Lth, Geq, Bt, Phi, Env
from dataflow import abstract_interp, liveness_constraint_gen
from collections import defaultdict


class IntersectionGraph:
    def __init__(s, program: list[Inst]):
        liveness = abstract_interp(liveness_constraint_gen(program))
        s.graph = defaultdict(lambda: set())
        s.mcsgraph = defaultdict(lambda: set())
        s.weights = dict()
        s.maxweight = 0
        # build intersection graph
        for values in liveness.values():
            for var in values:
                s.graph[var] |= set(values) - set([var])
                s.mcsgraph[var] |= set(values) - set([var])
        for var in s.graph.keys():
            s.weights[var] = 0
        s.weightedVs = sorted(s.weights.keys(), key=lambda x: s.weights[x])

    def N(s, v: str) -> set[str]:
        return s.graph[v]

    def pop(s):
        pop = s.weightedVs.pop(0)
        for n in s.mcsgraph[pop]:
            s.weights[n] += 1
        del s.mcsgraph[pop]
        del s.weights[pop]
        s.weightedVs = sorted(s.weights.keys(), key=lambda x: s.weights[x])
        for k in s.mcsgraph.keys():
            s.mcsgraph[k] -= set([pop])
        return pop

    def size(s):
        return len(s.mcsgraph)

    def greedy_coloring(s, sequence: list[str]) -> tuple[dict[str, int], int]:
        coloring = {var: 0 for var in s.graph.keys()}
        num_colors = 0
        for var in sequence:
            new_color = 0
            neighbour_colors = [coloring[n] for n in s.graph[var]]
            while new_color in neighbour_colors:
                new_color += 1
            coloring[var] = new_color
            if num_colors < new_color:
                num_colors = new_color
        return coloring, num_colors

    def maximum_cardinality_search(s):
        sequence = list()
        for i in range(s.size()):
            sequence.append(s.pop())
        return sequence


def register_allocation(prog: list[Inst]):
    """
    TODO: add descricao de phi aqui
        >>> prog, env = new_euclid()
        >>> coloring, num_registers = register_allocation(prog)
        >>> num_registers
        5
    """
    iGraph = IntersectionGraph(prog)
    return iGraph.greedy_coloring(iGraph.maximum_cardinality_search())


def new_euclid() -> list[Inst]:
    env = Env({
        'n0': 14, 'd': 5
    })
    i0 = Lth('z', 'n0', 'd')
    i2 = Mul('negd', 'd', -1)
    i3 = Phi('result1', 0, 'result2')
    i4 = Phi('n1', 'n0', 'n2')
    i5 = Add('result2', 'result1', 1)
    i6 = Add('n2', 'n1', 'negd')
    i7 = Geq('l', 'n2', 'd')
    i9 = Add('remainder', 0, 'n2')
    i10 = Add('end', 0, 0)
    i1 = Bt('z', i10)
    i8 = Bt('l', i3)
    prog = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
    for i in range(9):
        prog[i].add_next(prog[i+1])
    return prog, env
