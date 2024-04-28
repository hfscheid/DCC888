from lang import Env, Inst, BinOp, Bt, Add, Read, Mul, Lth, Geq
from abc import ABC, abstractmethod


class DataFlowEq(ABC):
    """
    A class that implements a data-flow equation. The key trait of a data-flow
    equation is an `eval` method, which evaluates that equation. The evaluation
    of an equation might change the environment that associates data-flow facts
    with identifiers.

    Attributes:
        num_evals the number of times that constraints have been evaluated.
            Remember to zero this attribute once you start a new static
            analysis, so that you can correctly count how many times each
            equation had to be evaluated to solve the analysis.
    """

    num_evals = 0

    def __init__(self, instruction):
        """
        Every data-flow equation is produced out of a program instruction. The
        initialization of the data-flow equation verifies if, indeed, the input
        object is an instruction.
        """
        assert isinstance(instruction, Inst)
        self.inst = instruction

    @classmethod
    @abstractmethod
    def name(self) -> str:
        """
        The name of a data-flow equation is used to retrieve the data-flow
        facts associated with that equation in the environment. For instance,
        imagine that we have an equation like this one below:

        "OUT[p] = (v, p) + (IN[p] - (v, _))"

        This equation affects OUT[p]. We store OUT[p] in a dictionary. The name
        of the equation is used as the key in this dictionary. For instance,
        the name of the equation could be 'OUT_p'.
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def deps(self) -> list:
        """
        A list with the name of all the constraints that this equation depends
        upon. For instance, if the equation is like:

        "OUT[p] = (v, p) + (IN[p] - (v, _))"

        Then, self.deps() == ['IN_p']
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def eval_aux(self, data_flow_env) -> set:
        """
        This method determines how each concrete equation evaluates itself.
        In a way, this design implements the 'template method' pattern. In other
        words, the DataFlowEq class implements a concrete method eval, which
        calls the abstract method eval_aux. It is the concrete implementation of
        eval_aux that determines how the environment is affected by the
        evaluation of a given equation.
        """
        raise NotImplementedError

    def eval(self, data_flow_env) -> bool:
        """
        This method implements the abstract evaluation of a data-flow equation.
        Notice that the actual semantics of this evaluation will be implemented
        by the `èval_aux` method, which is abstract.
        """
        DataFlowEq.num_evals += 1
        old_env = data_flow_env[self.name()]
        data_flow_env[self.name()] = self.eval_aux(data_flow_env)
        return True if data_flow_env[self.name()] != old_env else False


def name_in(ID):
    """
    The name of an IN set is always ID + _IN. Eg.:
        >>> Inst.next_index = 0
        >>> add = Add('x', 'a', 'b')
        >>> name_in(add.ID)
        'IN_0'
    """
    return f"IN_{ID}"

class SparseDataFlowEq(DataFlowEq):
    """
    When dealing with SSA-Form programs a classical data-flow analysis is
    somewhat cumbersome. Since every variable is associated with a single
    information during their whole lifetime, the analysis state can be shared
    across all program points. Thus, each instruction contributes to this state
    by defining the state of their own involved variable.

    This class inherits attributes from DataFlowEq.
    """

    @classmethod
    @abstractmethod
    def eval_aux(self, data_flow_env: dict):
        """
        This method determines how each concrete equation evaluates itself.
        Note that now the the reveived state is updated locally.
        """
        raise NotImplementedError

    def eval(self, data_flow_env: dict) -> bool:
        """
        This method implements the abstract evaluation of a data-flow equation.
        Notice that the actual semantics of this evaluation will be implemented
        by the `eval_aux` method, which is abstract.
        """
        DataFlowEq.num_evals += 1
        old_env = data_flow_env.copy()
        self.eval_aux(data_flow_env)
        return True if data_flow_env != old_env else False


class SparseConstantPropagation(SparseDataFlowEq):
    """
    This concrete class implements the sparse analysis for Constant
    Propagation. Since we assume an input program is in SSA Form, 
    there is no further need for IN and OUT sets for each instruction.
    Instead, each variable is associated with one state by the end of the
    Analysis.
    """

    def eval_aux(self, data_flow_env):
        """
        The evaluation of the meet operation over constant propagation follows
        the lattice:
                Not-a-constant (NAC)
              /   /   /  | \  \  \ 
            ... -c2 -c1 c0 c1 c2 ... 
              \   \   \  | /  /  /  
                Undefined (UNDEF)

        Whereby variables start UNDEF untill value assignment, operations with
        constants do not move them up the lattice and operations with NACs turn
        them into NACs as well.

        Each SparseConstantPropagation adds

        Example:
            >>> Inst.next_index = 0
            >>> i0 = Add('x', 'ZERO', 'ZERO')
            >>> i1 = Read('y')
            >>> i2 = Add('z', 'x', 'y')
            >>> i0.add_next(i1)
            >>> i1.add_next(i2)
            >>> df = SparseConstantPropagation(i2)
            >>> env = {'ZERO': 0, 'x': 0, 'y': 'NAC'}
            >>> df.eval_aux(env)
            >>> sorted(env.items())
            [('ZERO', 0), ('x', 0), ('y', 'NAC'), ('z', 'NAC')]
        """
        if type(self.inst) is Bt:
            return

        op = {
            Add:    lambda: self.inst.src0 + self.inst.src1,
            Mul:    lambda: self.inst.src0 * self.inst.src1,
            Bt:     lambda: 'NAC',
            Lth:    lambda: int(self.inst.src0 < self.isnt.src1),
            Geq:    lambda: int(self.inst.src0 >= self.isnt.src1),
            Read:   lambda: 'NAC',
        }

        vs = self.inst.uses()
        for v in vs:
            if data_flow_env[v] == 'NAC':
                data_flow_env[self.inst.definition().pop()] = 'NAC'
                return

        data_flow_env[self.inst.definition().pop()] = \
                op[type(self.inst)]()



def constant_prop_constraint_gen(instructions: list[Inst]):
    return [SparseConstantPropagation(i) for i in instructions]


def abstract_interp(equations):
    """
    This function iterates on the equations, solving them in the order in which
    they appear. It returns an environment with the solution to the data-flow
    analysis.

    Example for reaching-definition analysis:
        >>> Inst.next_index = 0
        >>> i0 = Add('c', 'a', 'b')
        >>> i1 = Mul('d', 'c', 'a')
        >>> i0.add_next(i1)
        >>> eqs = constant_prop_constraint_gen([i0, i1])
        >>> (sol, num_evals) = abstract_interp(eqs)
    """
    from functools import reduce

    DataFlowEq.num_evals = 0
    env = {eq.name(): set() for eq in equations}
    changed = True
    while changed:
        changed = reduce(lambda acc, eq: eq.eval(env) or acc, equations, False)
    return (env, DataFlowEq.num_evals)
