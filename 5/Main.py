import os
import sys
import re
import math

seatRe = re.compile('(?P<row>[FB]{7})(?P<col>[LR]{3})')

def mid(rangeMinMax, roundingFct):
    return roundingFct((rangeMinMax[1] - rangeMinMax[0]) / 2) + rangeMinMax[0]

class DataCheck():
    def __init__(self):
        # Row first, col second
        self.data = []
    
    def BinSplit(self, rangeNumber, lowChar, lineStr):
        if len(lineStr) <= 0:
            return rangeNumber[0]
        if lineStr[0] == lowChar:
            return self.BinSplit([rangeNumber[0], mid(rangeNumber, math.floor)], lowChar, lineStr[1:])
        return self.BinSplit([mid(rangeNumber, math.ceil), rangeNumber[1]], lowChar, lineStr[1:])
    
    def ParseLine(self, line):
        match = seatRe.match(line)
        if match:
            self.data.append([self.BinSplit([0, 127], 'F', match.group('row')), self.BinSplit([0, 8], 'L', match.group('col'))])
    
    def LoadInput(self):
        with open('input.txt') as inputFile:
            for line in inputFile:
                self.ParseLine(line.rstrip().lstrip())
    
    def CheckParseLine(self):
        self.ParseLine("BFFFBBFRRR")
        self.ParseLine("FFFBBBFRRR")
        self.ParseLine("BBFFBBFRLL")
        print("Check parse: ", self.data)
    
    def ConvertToScore(self):
        return map(lambda x: x[0] * 8 + x[1], self.data)
    
    def RunTest1(self):
        print("Test 1: ", max(self.ConvertToScore()))
    
    def RunTest2(self):
        scores = sorted(self.ConvertToScore())
        missing = [x for x in scores[1:-1] if not(((x - 1) in scores) and ((x + 1) in scores))]
        print("Test 2:", mid(missing, round))


if __name__ == "__main__":
    data = DataCheck()
    data.CheckParseLine()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
