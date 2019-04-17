class Memory():
    def __init__(self):
        self.__TuringTape__ = []
        self.__TuringTape__.append(0)
        self.__Pointer__ = 0

    def MoveRight(self):
        self.__Pointer__ += 1
        while self.__Pointer__ > self.__TuringTape__.__len__() - 1:
            self.__TuringTape__.append(0)

    def MoveLeft(self):
        if self.__Pointer__ <= 0:
            raise Exception("Memory Pointer Reached -1")
        else:
            self.__Pointer__ -= 1

    def SetValue(self, value):
        self.__TuringTape__[self.__Pointer__] = value

    def GetValue(self):
        return self.__TuringTape__[self.__Pointer__]

    def Increment(self):
        self.__TuringTape__[self.__Pointer__] += 1

    def Decrement(self):
        if self.__TuringTape__[self.__Pointer__] <= 0:
            raise Exception("Value at Pointer Address " + str(self.__Pointer__) + " reached -1")
        self.__TuringTape__[self.__Pointer__] -= 1