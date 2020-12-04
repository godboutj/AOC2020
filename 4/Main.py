import os
import sys
import re
from functools import reduce

fileLineRe = re.compile('\s+(?P<key>\S+):(?P<value>\S+)')

class DataCheck():
    def __init__(self):
        # Row first
        self.data = []
        self.LoadInput()
    
    def ParseData(self, cumul_data):
        matches = fileLineRe.findall(cumul_data)
        info = {}
        for m in matches:
            info[m[0]] = m[1]
        self.data.append(info)
    
    def LoadInput(self):
        with open('input.txt') as inputFile:
            cumul_data = ""
            for line in inputFile:
                if len(line.rstrip()) > 0:
                    cumul_data = cumul_data + " " + line.rstrip()
                else:
                    self.ParseData(cumul_data)
                    cumul_data = ""
            self.ParseData(cumul_data)
    
    def CheckData(self, entry):
        # cid is ignored
        return all(key in entry.keys() for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
        
    def RunTest1(self):
        print("Test 1 count: ", len(list(filter(lambda x: self.CheckData(x), self.data))))

if __name__ == "__main__":
    data = DataCheck()
    data.RunTest1()
