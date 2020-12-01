import re
import os
import sys

def RunTest1():
    print("Test 1")
    input_number = []
    with open('input.txt') as inputFile:
        line = inputFile.readline()
        while len(line) > 0:
            input_number.append(int(line))
            line = inputFile.readline()
    nb_elem = len(input_number)
    for i in range(0, nb_elem - 1):
        for j in range(i, nb_elem):
            if (input_number[i] + input_number[j]) == 2020:
                print("Solution: {0} {1} {2}".format(input_number[i], input_number[j], input_number[i] * input_number[j]))

def RunTest2():
    print("Test 2")
    input_number = []
    with open('input.txt') as inputFile:
        line = inputFile.readline()
        while len(line) > 0:
            input_number.append(int(line))
            line = inputFile.readline()
    nb_elem = len(input_number)
    for i in range(0, nb_elem - 1):
        for j in range(i, nb_elem):
            for k in range(j, nb_elem):
                if (input_number[i] + input_number[j] + input_number[k]) == 2020:
                    print("Solution: {0} {1} {2} {3}".format(input_number[i], input_number[j], input_number[k], input_number[i] * input_number[j] * input_number[k]))

if __name__ == "__main__":
    RunTest1()
    RunTest2()