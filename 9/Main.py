import os
import sys
import re
import math

class DataCheck():
    def __init__(self):
        self.data = []
        self.test = False
        self.windowSize = 5 if self.test else 25
        self.Result1 = 0
        self.Index1 = -1
    
    def ParseLine(self, line):
        try:
            self.data.append(int(line.rstrip()))
        except:
            print("Line is not integer: ", line)
    
    def LoadInput(self):
        with open('input2.txt' if self.test else 'input.txt') as inputFile:
            i = 0
            for line in inputFile:
                if len(line.rstrip()) > 0:
                    self.ParseLine(line)
    
    def CheckSum(self, value, subData):
        for i in range(0, len(subData) - 1):
            for j in range(i + 1, len(subData)):
                if subData[i] + subData[j] == value:
                    return True
        return False
    
    def RunTest1(self):
        for i in range(self.windowSize + 1, len(self.data)):
            if not self.CheckSum(self.data[i], self.data[i - self.windowSize: i]):
                print("Test 1: ", i, self.data[i])
                self.Result1 = self.data[i]
                self.Index1 = i
                return
        print("Nothing found!")
    
    def RangeSum(self, value, subData):
        for i in range(0, len(subData) - 1):
            for j in range(i + 1, len(subData)):
                dataWindow = subData[i:j+1]
                if sum(dataWindow) == value:
                    minValue = min(dataWindow)
                    maxValue = max(dataWindow)
                    print("Sum match: ", i, j, subData[i], subData[j], minValue, maxValue)
                    self.Result2 = minValue + maxValue
                    return True
        return False
    
    def RunTest2(self):
        # continuous can only be before or after no overlap, test both separatly
        if self.RangeSum(self.Result1, self.data[0:self.Index1]):
            print("Test 2: ", self.Result2)
        elif self.RangeSum(self.Result1, self.data[self.Index1 + 1:]):
            print("Test 2: ", self.Result2)
        else:
            print("No solution found")


if __name__ == "__main__":
    data = DataCheck()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
