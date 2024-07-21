from lang import Inst
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
    g = MCSGraph(program)
    sequence = list()
    for i in range(g.size()):
        sequence.append(g.pop())
    return sequence
