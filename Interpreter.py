import sys

from Memory import Memory


class Interpreter:
    def __init__(self, programm):
        self.__LoopStack__ = []
        self.__PC__ = 0
        legal = set('+-<>.,[]')
        self.__Programm__ = ''.join(c for c in programm if c in legal)
        self.__Memory__ = Memory()

    def Run(self):
        while self.__PC__ < self.__Programm__.__len__():
            if self.__Programm__[self.__PC__] == '+':
                self.__Memory__.Increment()
            elif self.__Programm__[self.__PC__] == '-':
                self.__Memory__.Decrement()
            elif self.__Programm__[self.__PC__] == '>':
                self.__Memory__.MoveRight()
            elif self.__Programm__[self.__PC__] == '<':
                self.__Memory__.MoveLeft()
            elif self.__Programm__[self.__PC__] == '[':
                if self.__Memory__.GetValue() > 0:
                    self.__LoopStack__.append(self.__PC__)
                else:
                    self.__GotoEndLoop__()
            elif self.__Programm__[self.__PC__] == ']':
                if self.__LoopStack__.__len__() <= 0:
                    raise Exception("Loop did not had a opening bracket")
                self.__PC__ = self.__LoopStack__.pop() - 1
            elif self.__Programm__[self.__PC__] == ".":
                sys.stdout.write(chr(self.__Memory__.GetValue()))
                sys.stdout.flush()
            elif self.__Programm__[self.__PC__] == ',':
                self.__Memory__.SetValue(ord(sys.stdin.read(1)))

            self.__PC__ += 1

    def __GotoEndLoop__(self):
        op = 0
        while 1:
            self.__PC__ += 1

            if self.__PC__ > self.__Programm__.__len__():
                raise Exception("No closing Bracket for Loop")

            if self.__Programm__[self.__PC__] == '[':
                op += 1
            elif self.__Programm__[self.__PC__] == ']':
                op -= 1

            if op < 0:
                return
