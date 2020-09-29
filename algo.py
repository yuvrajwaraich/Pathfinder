from DataStructures import Queue, Stack
from Position import Position
import pathfinder_gui


class Algorithms():

    def __init__(self):
        self.board = []
        self.startRow = 0
        self.startCol = 0
        self.finRow = 0
        self.finCol = 0
        self.numRow = 0
        self.numCol = 0
        self.finalPath = None

    def __setup(self):

        pBoard = pathfinder_gui.board
        self.numRow = len(pBoard)
        self.numCol = len(pBoard[0])
        self.board = [[Position(row, col) for col in range(self.numCol)]
                      for row in range(self.numRow)]
        self.startRow = 0
        self.startCol = 0
        self.finRow = 0
        self.finCol = 0
        self.finalPath = None

        for row in range(len(pBoard)):
            for col in range(len(pBoard[0])):
                if pBoard[row][col] == "S":
                    self.board[row][col].setType("START")
                    self.startRow = row
                    self.startCol = col
                elif pBoard[row][col] == "F":
                    self.board[row][col].setType("FINISH")
                    self.finRow = row
                    self.finCol = col
                elif pBoard[row][col] == "#":
                    self.board[row][col].setType("WALL")

    def Breadthfirst(self):
        self.__setup()
        queue = Queue()
        self.finalPath = None
        pathFound = False
        temp = None

        if self.board[self.startRow][self.startCol].getType() == "START":
            queue.enqueue(self.board[self.startRow][self.startCol])
            queue.getFront().getData().setVisited(True)

            while not queue.isEmpty() and not pathFound:
                temp = queue.dequeue().getData()

                if temp.getType() == "FINISH":
                    pathFound = True
                else:

                    if temp.getRow() > 0 and self.board[temp.getRow() - 1][temp.getCol()].getType() != "WALL"\
                            and self.board[temp.getRow() - 1][temp.getCol()].getVisited() == False:

                        self.board[temp.getRow() - 1][temp.getCol()
                                                      ].setVisited(True)
                        self.board[temp.getRow() - 1][temp.getCol()
                                                      ].setPrev(temp)
                        queue.enqueue(
                            self.board[temp.getRow() - 1][temp.getCol()])

                    if temp.getRow() < self.numRow - 1\
                            and self.board[temp.getRow() + 1][temp.getCol()].getType() != "WALL"\
                            and self.board[temp.getRow() + 1][temp.getCol()].getVisited() == False:

                        self.board[temp.getRow() + 1][temp.getCol()
                                                      ].setVisited(True)
                        self.board[temp.getRow() + 1][temp.getCol()
                                                      ].setPrev(temp)
                        queue.enqueue(
                            self.board[temp.getRow() + 1][temp.getCol()])

                    if temp.getCol() > 0 and self.board[temp.getRow()][temp.getCol() - 1].getType() != "WALL"\
                            and self.board[temp.getRow()][temp.getCol() - 1].getVisited() == False:

                        self.board[temp.getRow()][temp.getCol() -
                                                  1].setVisited(True)
                        self.board[temp.getRow()][temp.getCol() -
                                                  1].setPrev(temp)
                        queue.enqueue(
                            self.board[temp.getRow()][temp.getCol() - 1])

                    if temp.getCol() < self.numCol - 1\
                            and self.board[temp.getRow()][temp.getCol() + 1].getType() != "WALL"\
                            and self.board[temp.getRow()][temp.getCol() + 1].getVisited() == False:

                        self.board[temp.getRow()][temp.getCol() +
                                                  1].setVisited(True)
                        self.board[temp.getRow()][temp.getCol() +
                                                  1].setPrev(temp)
                        queue.enqueue(
                            self.board[temp.getRow()][temp.getCol() + 1])
                pathfinder_gui.showQueue(temp, queue)

        if pathFound:
            self.finalPath = Stack()

            while temp != None:
                self.finalPath.push(temp)
                temp = temp.getPrev()

            pathfinder_gui.showPath(self.finalPath)

    def Depthfirst(self):
        self.__setup()
        stack = Stack()
        temp = None
        pathFound = False
        self.finalPath = None

        if self.board[self.startRow][self.startCol].getType() == "START":
            stack.push(self.board[self.startRow][self.startCol])
            stack.getTop().getData().setVisited(True)

            while not stack.isEmpty() and not pathFound:
                temp = stack.pop().getData()

                if temp.getType() == "FINISH":
                    pathFound = True
                else:

                    if temp.getRow() > 0 and self.board[temp.getRow() - 1][temp.getCol()].getType() != "WALL"\
                            and self.board[temp.getRow() - 1][temp.getCol()].getVisited() == False:

                        self.board[temp.getRow() - 1][temp.getCol()
                                                      ].setVisited(True)
                        self.board[temp.getRow() - 1][temp.getCol()
                                                      ].setPrev(temp)
                        stack.push(
                            self.board[temp.getRow() - 1][temp.getCol()])

                    if temp.getRow() < self.numRow - 1\
                            and self.board[temp.getRow() + 1][temp.getCol()].getType() != "WALL"\
                            and self.board[temp.getRow() + 1][temp.getCol()].getVisited() == False:

                        self.board[temp.getRow() + 1][temp.getCol()
                                                      ].setVisited(True)
                        self.board[temp.getRow() + 1][temp.getCol()
                                                      ].setPrev(temp)
                        stack.push(
                            self.board[temp.getRow() + 1][temp.getCol()])

                    if temp.getCol() > 0 and self.board[temp.getRow()][temp.getCol() - 1].getType() != "WALL"\
                            and self.board[temp.getRow()][temp.getCol() - 1].getVisited() == False:

                        self.board[temp.getRow()][temp.getCol() -
                                                  1].setVisited(True)
                        self.board[temp.getRow()][temp.getCol() -
                                                  1].setPrev(temp)
                        stack.push(self.board[temp.getRow()]
                                   [temp.getCol() - 1])

                    if temp.getCol() < self.numCol - 1\
                            and self.board[temp.getRow()][temp.getCol() + 1].getType() != "WALL"\
                            and self.board[temp.getRow()][temp.getCol() + 1].getVisited() == False:

                        self.board[temp.getRow()][temp.getCol() +
                                                  1].setVisited(True)
                        self.board[temp.getRow()][temp.getCol() +
                                                  1].setPrev(temp)
                        stack.push(self.board[temp.getRow()]
                                   [temp.getCol() + 1])
                pathfinder_gui.showStack(temp, stack)

        if pathFound:
            self.finalPath = Stack()

            while temp != None:
                self.finalPath.push(temp)
                temp = temp.getPrev()
            pathfinder_gui.showPath(self.finalPath)

    def aStar(self):
        self.__setup()

        availNodes = []
        usedNodes = []
        availNodes.append(self.board[self.startRow][self.startCol])

        pathFound = False
        while not pathFound and len(availNodes) > 0:
            neighbours = []
            currNode = availNodes[0]
            availNodes.remove(currNode)
            usedNodes.append(currNode)

            if currNode.getType() == "FINISH":  # path has been found
                pathFound = True
            else:
                if currNode.getRow() > 0 and self.board[currNode.getRow() - 1][currNode.getCol()].getType() != "WALL":
                    neighbours.append(
                        self.board[currNode.getRow() - 1][currNode.getCol()])

                if currNode.getCol() > 0 and self.board[currNode.getRow()][currNode.getCol() - 1].getType() != "WALL":
                    neighbours.append(
                        self.board[currNode.getRow()][currNode.getCol() - 1])

                if currNode.getRow() < self.numRow - 1 and self.board[currNode.getRow() + 1][currNode.getCol()].getType() != "WALL":
                    neighbours.append(
                        self.board[currNode.getRow() + 1][currNode.getCol()])

                if currNode.getCol() < self.numCol - 1 and self.board[currNode.getRow()][currNode.getCol() + 1].getType() != "WALL":
                    neighbours.append(
                        self.board[currNode.getRow()][currNode.getCol() + 1])

                for neighbour in neighbours:
                    if neighbour not in usedNodes and (currNode.getGCost() + 10 < neighbour.getGCost() or neighbour not in availNodes):
                        neighbour.setGCost(currNode.getGCost() + 10)
                        neighbour.setHCost(int(((abs(neighbour.getRow() - self.finRow)**2 +
                                                 abs(neighbour.getCol() - self.finCol)**2)**(0.5))*10))

                        neighbour.setPrev(currNode)
                        if neighbour not in availNodes:
                            self.__sortedInsert(availNodes, neighbour)
            pathfinder_gui.showAStar(currNode, availNodes)

        if pathFound:
            self.finalPath = Stack()

            while currNode != None:
                self.finalPath.push(currNode)
                currNode = currNode.getPrev()

            pathfinder_gui.showPath(self.finalPath)

    def __sortedInsert(self, toAddto, elem):

        for a in range(len(toAddto)):
            if elem.getFCost() < toAddto[a].getFCost():
                toAddto.insert(a, elem)
                return
            elif elem.getFCost() == toAddto[a].getFCost():
                if elem.getHCost() < toAddto[a].getHCost():
                    toAddto.insert(a, elem)
                else:
                    toAddto.insert(a + 1, elem)
                return
        toAddto.append(elem)

    def toString(self):
        array = [["" for x in range(self.numCol)] for y in range(self.numRow)]
        info, pathInfo, pathCoord = "", "", ""
        temp = None

        if self.finalPath != None:
            pathCoord = "Path from start to finish:\n"

            while not self.finalPath.isEmpty():
                temp = self.finalPath.pop().getData()

                if temp.getType() == "PATH":
                    array[temp.getRow()][temp.getCol()] = "*"
                    pathCoord += temp.toString() + "\n"

            for x in range(self.numRow):
                for y in range(self.numCol):
                    if array[x][y] == "":
                        array[x][y] = self.board[x][y].getTypeString()
                    pathInfo += array[x][y]
                pathInfo += "\n"

            info = pathInfo + pathCoord + "\n"
        elif self.finalPath == None:
            info = "Path not found."

        return info
