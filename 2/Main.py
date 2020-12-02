import re
import os
import sys

fileLineRe = re.compile('(?P<min>[0-9]+)\s*\-\s*(?P<max>[0-9]+)\s*(?P<letter>[a-zA-Z]+)\s*:\s*(?P<input>\w+)')

class Rules:
    def __init__(self, count_min, count_max, letter):
        self.min = min(count_min, count_max)
        self.max = max(count_min, count_max)
        self.letter = letter
    
    def Validate1(self, input):
        nb = len(re.findall(self.letter, input))
        return nb >= self.min and nb <= self.max
    
    def CheckLetter(self, pos, input):
        i = pos - 1 # no index 0
        return i < len(input) and input[i] == self.letter
    
    def Validate2(self, input):
        return self.CheckLetter(self.min, input) != self.CheckLetter(self.max, input)


def RunTest():
    successTest1 = 0
    successTest2 = 0
    with open('input.txt') as inputFile:
        line = inputFile.readline()
        while len(line) > 0:
            match = fileLineRe.match(line)
            if match:
                rule = Rules(int(match.group('min')), int(match.group('max')), match.group('letter'))
                str_input = match.group('input')
                if rule.Validate1(str_input):
                    successTest1 += 1
                if rule.Validate2(str_input):
                    successTest2 += 1
            line = inputFile.readline()
    print("Test 1 nb success: " + str(successTest1))
    print("Test 2 nb success: " + str(successTest2))

if __name__ == "__main__":
    RunTest()
