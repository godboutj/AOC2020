import os
import sys
import re
import math
import networkx
from networkx.algorithms.traversal import dfs_predecessors, dfs_successors
from functools import reduce

mainBagRe = re.compile('^(?P<colorMain>\S+\s+\S+)(\s+bags\s+contain\s+)(?P<contain>.*)\.?$')
subBagRe = re.compile('\s*(?P<nb>[0-9]+)\s+(?P<color>\S+\s+\S+)\s*bag[s]?[,.]?')
noOtherRe = re.compile('no other bags.')

class DataCheck():
    def __init__(self):
        self.graph = networkx.MultiDiGraph()
        self.graphRev = networkx.MultiDiGraph()
    
    def AddNode(self, color):
        self.graph.add_node(color)
        self.graphRev.add_node(color)
    
    def AddEdge(self, fromColor, toColor, nb):
        self.graph.add_edge(fromColor, toColor, weight=nb)
        self.graphRev.add_edge(toColor, fromColor, weight=nb)
    
    def ParseLine(self, line):
        match = mainBagRe.match(line)
        if match:
            containerColor = match.group('colorMain')
            self.AddNode(containerColor)
            containLine = match.group('contain')
            matchColor = subBagRe.findall(containLine)
            if len(matchColor) == 0:
                if not noOtherRe.match(containLine):
                    print('missing: ', containLine, line)
            else:
                for m in matchColor:
                    nbSub = m[0]
                    subColor = m[1]
                    self.AddNode(subColor)
                    self.AddEdge(containerColor, subColor, nbSub)
        else:
            print("Parse line failure: ", line)
    
    def LoadInput(self):
        with open('input.txt') as inputFile:
            i = 0
            for line in inputFile:
                if len(line.rstrip()) > 0:
                    self.ParseLine(line)
    
    def RunTest1(self):
        print("Test 1: ", len(dfs_predecessors(self.graphRev, 'shiny gold').keys()))
    
    def FindSuccessor(self, node_name):
        sub = []
        for nbr in self.graph[node_name]:
            sub.append(nbr)
        return sub
    
    def NbContain(self, node_name):
        contain = 0
        for p in self.FindSuccessor(node_name):
            w = int(self.graph.get_edge_data(node_name, p)[0]['weight'])
            contain += w
            nbsub = self.NbContain(p)
            contain += w * nbsub
        return contain
    
    def RunTest2(self):
        print("Test 2: ", self.NbContain('shiny gold'))


if __name__ == "__main__":
    data = DataCheck()
    data.LoadInput()
    data.RunTest1()
    data.RunTest2()
