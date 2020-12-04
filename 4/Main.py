import os
import sys
import re
from functools import reduce

fileLineRe = re.compile('\s+(?P<key>\S+):(?P<value>\S+)')
heightRe = re.compile('(?P<value>[0-9]+)(?P<unit>in|cm)')
hairRe = re.compile('^#[0-9a-f]{6}$')
eyeRe = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pidRe = re.compile('^[0-9]{9}$')

def CheckRegex(entry, regex):
    match = regex.match(entry)
    if match:
        return True
    return False

def CheckNbLetter(entry, min, max):
    return len(entry) >= min and len(entry) <= max

def CheckNumber(entry, min, max):
    try:
        val = int(entry)
        return val >= min and val <= max
    except:
        return False

def CheckHeight(entry):
    match = heightRe.match(entry)
    if match:
        unit = match.group('unit')
        value = int(match.group('value'))
        if unit == 'cm':
            return value >= 150 and value <= 193
        elif unit == 'in':
            return value >= 59 and value <= 76
    return False

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
    
    def CheckData2(self, entry):
        validation = {
            "byr": lambda x: CheckNbLetter(x, 4, 4) and CheckNumber(x, 1902, 2002),
            "iyr": lambda x: CheckNbLetter(x, 4, 4) and CheckNumber(x, 2010, 2020),
            "eyr": lambda x: CheckNbLetter(x, 4, 4) and CheckNumber(x, 2020, 2030),
            "hgt": lambda x: CheckHeight(x),
            "hcl": lambda x: CheckRegex(x, hairRe),
            "ecl": lambda x: CheckRegex(x, eyeRe),
            "pid": lambda x: CheckRegex(x, pidRe)
        }
        return all(key in entry.keys() and validation[key](entry[key]) for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) 
    
    def RunTest2(self):
        print("Test 2 count: ", len(list(filter(lambda x: self.CheckData2(x), self.data))))

if __name__ == "__main__":
    data = DataCheck()
    data.RunTest1()
    data.RunTest2()
