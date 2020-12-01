import re
import os
import sys

def LoadData():
    input_number = []
    with open('input.txt') as inputFile:
        line = inputFile.readline()
        while len(line) > 0:
            input_number.append(int(line))
            line = inputFile.readline()
    return input_number

def RunTest1(input_number):
    print("Test 1")
    nb_elem = len(input_number)
    for i in range(0, nb_elem - 1):
        for j in range(i + 1, nb_elem):
            if (input_number[i] + input_number[j]) == 2020:
                print("Solution: {0} {1} {2}".format(input_number[i], input_number[j], input_number[i] * input_number[j]))

def RunTest2(input_number):
    print("Test 2")
    nb_elem = len(input_number)
    for i in range(0, nb_elem - 2):
        for j in range(i + 1, nb_elem):
            for k in range(j + 1, nb_elem):
                if (input_number[i] + input_number[j] + input_number[k]) == 2020:
                    print("Solution: {0} {1} {2} {3}".format(input_number[i], input_number[j], input_number[k], input_number[i] * input_number[j] * input_number[k]))

if __name__ == "__main__":
    data = LoadData()
    RunTest1(data)
    RunTest2(data)