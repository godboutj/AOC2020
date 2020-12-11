import os
import sys
import re
import math

instructionRe = re.compile('^(?P<instruction>(nop|acc|jmp))\s+(?P<amount>[+-][0-9]+)')

class InstructionRun():
    def __init__(self):
        self.accumulate = 0
    
    def nop(self, x, index):
        return index + 1
    
    def acc(self, x, index):
        self.accumulate += x
        return index + 1
    
    def jmp(self, x, index):
        return index + x

class DataCheck():
    def __init__(self):
        self.data = []
        self.mementoData = []
        self.Reset()
    
    def Reset(self):
        self.stack = []
        self.instructions = InstructionRun()
    
    def ParseLine(self, line):
        match = instructionRe.match(line)
        if match:
            instruction = match.group('instruction')
            amount = int(match.group('amount'))
            self.data.append((instruction, amount))
        else:
            print("Parse line failure: ", line)
    
    def LoadInput(self):
        with open('input.txt') as inputFile:
            i = 0
            for line in inputFile:
                if len(line.rstrip()) > 0:
                    self.ParseLine(line)
    
    def Execute(self, index):
        if index == len(self.data):
            print("program completed!")
            return True
        elif index > len(self.data):
            # Assum program is completed when we reach the end
            print("Index out of program: ", index)
            return False
        if index in self.stack:
            print("Infinit loop: ", index)
            return False
        self.stack.append(index)
        info = self.data[index]
        next_index = getattr(self.instructions, info[0])(info[1], index)
        return self.Execute(next_index)
    
    def RunTest1(self):
        self.Reset()
        if not self.Execute(0):
            print("Test 1: ", self.stack[-1], self.instructions.accumulate)
        else:
            print("Test 1: ", "program completed")
    
    def SwapNextInstruction(self, start):
        for i in range(start, len(self.data)):
            if self.data[i][0] == 'nop':
                self.data[i] = ('jmp', self.data[i][1])
                return i
            elif self.data[i][0] == 'jmp':
                self.data[i] = ('nop', self.data[i][1])
                return i
        # no solution found!
        return len(self.data) + 1
    
    def TestData(self, start_index):
        self.data = self.mementoData.copy()
        index = self.SwapNextInstruction(start_index)
        self.Reset()
        if self.Execute(0):
            return (True, index)
        return (False, index + 1) # Move to next index next time
    
    def RunTest2(self):
        self.mementoData = self.data.copy()
        index = 0
        success = False
        while not success and index < len(self.data):
            success, index = self.TestData(index)
        self.data = self.mementoData.copy()
        print("Test 2: success: ", success, " replace index:", index, " acc: ", self.instructions.accumulate)


if __name__ == "__main__":
    data = DataCheck()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
