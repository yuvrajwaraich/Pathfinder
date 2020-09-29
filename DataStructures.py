class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, item):
        if self.first == None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.setNext(Node(item))
            self.last = self.last.getNext()
        self.size += 1

    def dequeue(self):
        currNode = self.first
        self.first = self.first.getNext()
        self.size -= 1
        return currNode

    def isEmpty(self):
        return self.size == 0

    def getFront(self):
        return self.first

    def getSize(self):
        return self.size

    def clear(self):
        while self.first != None:
            self.first = self.first.getNext()
        self.size = 0

    def toString(self):
        string = ""
        travNode = self.first
        while travNode != None:
            string += travNode.toString() + '\n'
        return string


class Stack():

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        node = Node(item, self.top)
        self.top = node
        self.size += 1

    def pop(self):
        currNode = self.top
        self.top = self.top.getNext()
        self.size -= 1
        return currNode

    def isEmpty(self):
        return self.size == 0

    def getTop(self):
        return self.top

    def getSize(self):
        return self.size

    def clear(self):
        while self.top != None:
            self.top = self.top.getNext()
        self.size = 0

    def toString(self):
        string = ""
        travNode = self.top
        while travNode != None:
            string += travNode.toString() + '\n'
        return string


class Node:

    def __init__(self, item, nextNode=None):
        self.data = item
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, node):
        self.nextNode = node

    def toString(self):
        return self.data.toString()
