import sys

from Interpreter import Interpreter

if sys.argv.__len__() < 2:
    raise Exception("No Brainfck File specified")

code = open(sys.argv[1], 'r')
with code:
    prg = code.read().replace('\n', '')

interpreter = Interpreter(prg)
interpreter.Run()