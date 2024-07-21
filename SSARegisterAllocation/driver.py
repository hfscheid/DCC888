from lang import interp
from graph import new_euclid

prog, env = new_euclid()
res = interp(prog[0], env)
res.dump()
