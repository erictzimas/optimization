import random
import math

def objcoeff(matrix):
        s = 0
        k = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                s += matrix[i][j]
            k += s
        return k

class Model:
# instance variables
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

# Objective coefficient

    def BuildModel(self, seed):  # FIXME Added seed argument for testing purposes. Change back.
        random.seed(seed)  # FIXME
        depot = Node(0, 0, 0, 50, 50)  # FIXED -- 0 service_time instead of 15
        self.allNodes.append(depot)
        self.capacity = 50
        totalCustomers = 100
        for i in range (0, totalCustomers):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            dem = random.randint(1, 150)  # FIXED -- 1-150 instead of 1-1500
            cust = Node(i + 1, 0.25, dem, x, y)  # FIXED -- 0.25 of an hour instead of 15 minutes. If time in minutes is needed, also change maxHours to maxMinutes in Solver.NaiveConstructive
            self.allNodes.append(cust)
            self.customers.append(cust)

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist
        print(objcoeff(self.matrix))
    


class Node:
    def __init__(self, id, st, dem, xx, yy):
        self.id = id
        self.service_time = st
        self.demand = dem
        self.x = xx
        self.y = yy 

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.capacity = cap
        self.load = 0