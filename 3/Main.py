import os
import sys
from functools import reduce

class DataGrid():
    def __init__(self):
        # Row first
        self.data = []
        self.LoadInput()
    
    def LoadInput(self):
        with open('input.txt') as inputFile:
            line = inputFile.readline()
            while len(line) > 0:
                data_line = []
                for pos in line:
                    if pos == '.':
                        data_line.append(0)
                    elif pos == '#':
                        data_line.append(1)
                # TODO godboutj 2020-12-03, add sanity check for nb columns
                self.data.append(data_line)
                line = inputFile.readline()
    
    def NbColumn(self):
        return len(self.data[0])
    
    def NbRow(self):
        return len(self.data)
    
    def NbObjectAt(self, row, col):
        # wrap around on the column axis
        if row < self.NbRow():
            return self.data[row][col % self.NbColumn()]
        return 0

def ElemListFct(list1, list2, fct):
    return [fct(x, list2[i]) for i,x in enumerate(list1)] 
    
def SumList(list1, list2):
    fct = lambda e1, e2: e1 + e2
    return ElemListFct(list1, list2, fct)

def CheckSlope(data, vector):
    treeCount = 0
    pos = [0,0]
    while pos[0] < data.NbRow():
        treeCount += data.NbObjectAt(pos[0], pos[1])
        #print('pos : ', pos, ' nb tree: ', treeCount)
        pos = SumList(pos, vector)
    return treeCount

def RunTest1(data):
    treeCount = CheckSlope(data, [1,3])
    print('Tree count: ', treeCount)

def RunTest2(data):
    treeCountList = map(lambda x: CheckSlope(data, x), [[1,1], [1,3], [1,5], [1,7], [2,1]])
    total = reduce(lambda x,y: x * y, treeCountList)
    print("Total", total)

if __name__ == "__main__":
    data = DataGrid()
    RunTest1(data)
    RunTest2(data)
