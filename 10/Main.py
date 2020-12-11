import os
import sys
import re
import math

class DataCheck():
    def __init__(self):
        self.data = []
        self.test = False
        self.maxJolt = 0
        self.diffJolt = [0, 0, 0, 0]
    
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
        self.PrepareData()
    
    def PrepareData(self):
        self.data.sort()
        self.maxJolt = self.data[-1] + 3
        print("Max Jolt: ", self.maxJolt)
    
    def ValidateJolt(self, jolt, data):
        delta = data[0] - jolt
        if delta > 3:
            raise Exception("more then 3 jolts between adaptor!")
        self.diffJolt[delta] += 1
        return data[0]
    
    def RunTest1(self):
        jolt = 0
        currentData = self.data
        currentData.append(self.maxJolt)
        try:
            while len(currentData) > 0:
                jolt = self.ValidateJolt(jolt, currentData)
                currentData.pop(0)
            print("Test 1: ", self.diffJolt, self.diffJolt[1] * self.diffJolt[3])
        except:
            print("Invalid gap, cannot use all adaptors")
    
    def RunTest2(self):
        print("Test 2: ")

if __name__ == "__main__":
    data = DataCheck()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
