import lang
import parser
import sys

lines = sys.stdin.readlines()
env, prog = parser.file2cfg_and_env(lines)
lang.type_interp(prog[0], lang.TypeEnv.from_env(env))
