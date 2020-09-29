class Position():

    def __init__(self, row, col, squareType="PATH", prev=None, g_cost=0, h_cost=0):
        self.row = row
        self.col = col
        self.squareType = squareType
        self.prev = prev
        self.visited = False
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getType(self):
        return self.squareType

    def setType(self, newType):
        self.squareType = newType

    def getTypeString(self):
        if self.squareType == "START":
            return "S"
        elif self.squareType == "FINISH":
            return "F"
        elif self.squareType == "WALL":
            return "#"
        else:
            return "."

    def getPrev(self):
        return self.prev

    def setPrev(self, pos):
        self.prev = pos

    def getVisited(self):
        return self.visited

    def setVisited(self, value):
        self.visited = value

    def getGCost(self):
        return self.g_cost

    def setGCost(self, newCost):
        self.g_cost = newCost
        self.f_cost = self.g_cost + self.h_cost

    def getHCost(self):
        return self.h_cost

    def setHCost(self, newCost):
        self.h_cost = newCost
        self.f_cost = self.g_cost + self.h_cost

    def getFCost(self):
        return self.f_cost

    def toString(self):
        return f'coords = {self.row, self.col}, SquareType = "{self.squareType}"'
