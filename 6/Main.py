import os
import sys
import re
import math
from functools import reduce

letterRe = re.compile('(?P<letter>[a-z]{1})')

class DataCheck():
    def __init__(self):
        # Row first, col second
        self.data = []
        self.AnyData = []
        self.AllData = []
        self.ResetEntries()
    
    def ResetEntries(self):
        self.entries = {}
        self.nbPerson = 0
    
    def ParsePerson(self, line):
        allletter = letterRe.findall(line)
        for l in allletter:
            if l not in self.entries:
                self.entries[l] = 0
            self.entries[l] += 1
    
    def GatherGroup(self):
        self.data.append([self.nbPerson, self.entries])
        self.AnyData.append(len(self.entries.keys()))
        self.AllData.append(len([k for k, v in self.entries.items() if v == self.nbPerson]))
        self.ResetEntries()
        
    def LoadInput(self):
        with open('input.txt') as inputFile:
            cumul_data = ""
            for line in inputFile:
                if len(line.rstrip()) > 0:
                    self.ParsePerson(line)
                    self.nbPerson += 1
                else:
                    self.GatherGroup()
            self.GatherGroup()
    
    def TestAlgo(self):
        print("ABC test: ", self.ParseData("abc"))
    
    def RunTest1(self):
        print("Test 1: ", reduce(lambda x,y: x + y, self.AnyData))
    
    def RunTest2(self):
        print("Test 2: ", reduce(lambda x,y: x + y, self.AllData))


if __name__ == "__main__":
    data = DataCheck()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
