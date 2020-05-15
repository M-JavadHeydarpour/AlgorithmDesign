# BFS +
# DFS +
# bipartite +
# strongConnectivity -
# Dijkstra +
# Prim +
# Kruskal -

import Heap
import sys


class Graph:
    def __init__(self):
        # graph = {
        #     'A': ['B', 'S', 'C'],
        #     'B': ['A'],
        #     'C': ['D', 'E', 'F', 'S', 'A'],
        #     'D': ['C'],
        #     'E': ['C', 'H'],
        #     'F': ['C', 'G'],
        #     'G': ['F', 'S'],
        #     'H': ['E', 'G'],
        #     'S': ['A', 'C', 'G']
        # }

        self.graph = {
            'A': ['B', 'D'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['A', 'C'],
            # 'H': ['G'],
            # 'G': ['H'],
        }
        # self.weightedGraph = {
        #     'A': {'A': -1, 'B': 5, 'D': 3, 'E': 12, 'F': 5},
        #     'B': {'B': -1, 'A': 5, 'D': 1, 'G': 2},
        #     'C': {'C': -1, 'G': 2, 'E': 1, 'F': 16},
        #     'D': {'D': -1, 'B': 1, 'G': 1, 'E': 1, 'A': 3},
        #     'E': {'E': -1, 'A': 12, 'D': 1, 'C': 1, 'F': 2},
        #     'F': {'F': -1, 'A': 5, 'E': 2, 'C': 16},
        #     'G': {'G': -1, 'B': 2, 'D': 1, 'C': 2}
        # }

        self.weightedGraph = {
            'A': {'A': -1, 'B': 1, 'D': 2},
            'B': {'B': -1, 'A': 1, 'C': 7},
            'C': {'C': -1, 'D': 4, 'B': 7},
            'D': {'D': -1, 'A': 2, 'B': 3, 'C': 4}
        }

        self.vertexCount = 7

        self.priorityQueue = Heap.PriorityQueue(self.vertexCount)  # allocate a heap tree for priority Queue

        self.MAXINT = sys.maxsize  # positive inf value
        # self.MININT = -sys.maxsize - 1  # negative inf value

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def dfs(self, graph, node='A', tag=[]):

        if node not in tag:
            tag.append(node)

            for n in graph[node]:
                self.dfs(graph, n, tag)

        return tag

    def bfs(self, graph, node='A', tag=None):

        if tag is None:
            tag = []

        queue = [node]
        # tag = [node]
        # tag.append(node)

        while queue:

            signed = queue.pop(0)
            # tag.append(signed)
            if signed not in tag:
                tag.append(signed)
                # print(signed, end=" ")

                for neighbour in self.graph[signed]:
                    # if neighbour not in tag:
                    queue.append(neighbour)
                    # tag.append(neighbour)
        return tag

    def isBipartite(self, graph, node='A'):

        queue = [node]
        keys = self.graph.keys()
        value = [-1] * len(self.graph.keys())
        colorDict = dict(zip(keys, value))

        while queue:

            signed = queue.pop(0)

            if signed in self.graph[signed]:
                return False

            for vertex in self.graph.keys():

                if vertex in self.graph[signed] and colorDict[vertex] == -1:

                    colorDict[vertex] = 1 - colorDict[signed]
                    queue.append(vertex)

                elif vertex in self.graph[signed] and colorDict[vertex] == colorDict[signed]:
                    return False

        return True

    # [priority, data]
    def Dijkstra(self, startingPoint='A'):

        # initialize the queue and insert nodes with inf value
        for key in self.weightedGraph.keys():
            if key == startingPoint:
                self.weightedGraph[key][key] = 0
                self.priorityQueue.insert(0, startingPoint)
            else:
                self.weightedGraph[key][key] = self.MAXINT
                self.priorityQueue.insert(self.MAXINT, key)

        while not self.priorityQueue.isEmpty():  # while queue not is empty

            minVertex = self.priorityQueue.delete()
            minVertex = minVertex[1]

            minValue = self.MAXINT
            resTemp = minValue

            # rangeList = list(self.weightedGraph[minVertex[1]].values())
            rangeList = list(self.weightedGraph[minVertex])
            # rangeList = rangeList[1:]
            # for edge in self.weightedGraph[minVertex[1]].values():
            for edge in rangeList:
                if edge != minVertex:
                    # print(self.weightedGraph[edge])
                    # print(self.weightedGraph[edge][edge])
                    if self.weightedGraph[edge][edge] > self.weightedGraph[minVertex][minVertex] + \
                            self.weightedGraph[minVertex][edge]:
                        # mokafat asli :/
                        self.weightedGraph[edge][edge] = self.weightedGraph[minVertex][minVertex] + \
                                                         self.weightedGraph[minVertex][edge]
                        # if self.weightedGraph[edge][edge] < minValue:
                        # minValue = self.weightedGraph[edge][edge]
                        # resTemp = edge
            # if resTemp != self.MAXINT:
            #     self.result[minVertex] = resTemp

            temp = []
            while not self.priorityQueue.isEmpty():
                temp.append(self.priorityQueue.delete()[1])
            for item in temp:
                self.priorityQueue.insert(self.weightedGraph[item][item], item)
        print("Vertex\tDistance from source\n")
        for item in self.weightedGraph:
            print(list(self.weightedGraph[item].keys())[0], '\t\t\t', self.weightedGraph[item][item], '\n')

    # [priority, data]
    def Prim(self, startingPoint='A'):

        # initialize the queue and insert nodes with inf value
        for key in self.weightedGraph.keys():
            if key == startingPoint:
                self.weightedGraph[key][key] = 0
                self.priorityQueue.insert(0, startingPoint)
            else:
                self.weightedGraph[key][key] = self.MAXINT
                self.priorityQueue.insert(self.MAXINT, key)

        while not self.priorityQueue.isEmpty():  # while queue not is empty

            minVertex = self.priorityQueue.delete()
            minVertex = minVertex[1]

            minValue = self.MAXINT

            rangeList = list(self.weightedGraph[minVertex])

            for edge in rangeList:
                if edge != minVertex:

                    if self.weightedGraph[edge][edge] > self.weightedGraph[minVertex][edge]:
                        self.weightedGraph[edge][edge] = self.weightedGraph[minVertex][edge]
                        # if self.weightedGraph[edge][edge] < minValue:
                        #     minValue = self.weightedGraph[edge][edge]

            temp = []
            while not self.priorityQueue.isEmpty():
                temp.append(self.priorityQueue.delete()[1])
            for item in temp:
                self.priorityQueue.insert(self.weightedGraph[item][item], item)

        print("Vertex\tEdge selected value\n")
        for item in self.weightedGraph:
            print(list(self.weightedGraph[item].keys())[0], '\t\t\t', self.weightedGraph[item][item], '\n')

    def utility(self, parent, item):
        pass

    def union(self):
        pass

    def Kruskal(self):
        pass


if __name__ == "__main__":
    gp = Graph()
    # gp.Dijkstra()
    # gp.Prim()
    # gp.Kruskal()
    # gp.test()
    # result = gp.dfs(gp.graph)
    # result = gp.bfs(gp.graph)
    # result = gp.isBipartite(gp.graph)
    # print(result)
