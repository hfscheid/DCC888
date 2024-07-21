from parser import file2cfg_and_env
from lang import interp


def run():
    with open('euclid.txt', 'r') as f:
        lines = f.readlines()

    env, prog = file2cfg_and_env(lines)
    result = interp(prog[0], env)
    result.dump()


def run_ssa():
    with open('euclid-ssa.txt', 'r') as f:
        lines = f.readlines()

    env, prog = file2cfg_and_env(lines)
    result = interp(prog[0], env)
    result.dump()
