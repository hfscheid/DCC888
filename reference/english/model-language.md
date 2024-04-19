# Model Language
The model language contains few instructions, that however are sufficient to
build turing-complete programs. It contains 5 commands:
    - `Add(x, a, b)`: implements x = a + b
    - `Mul(x, a, b)`: implements x = a * b
    - `Lth(x, a, b)`: implements x = (a < b) ? 1 : 0
    - `Geq(x, a, b)`: implements x = (a >= b) ? 1 : 0
    - `Bt(x, i0, i1)`: if x != 0, then executes instruction i0, else executed i1

Through all tasks programs will be represented as Python Lists of these 
instructions. A special function `interp(instruction, environment)` is
responsible for executing such programs. It requires both program and an
environment, which is specified as a Dict[str, int].

## Implementation
All instructions descend from the `Inst` class.
