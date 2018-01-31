from BinarySearch.Node import Node


class  BST(object):

    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else: 
            self.rootNode.insert(data)


    def remove(self, dataToremove):
        if self.rootNode:
            if self.rootNode.data == dataToremove:
                tempNode = Node(None)
                tempNode.leftChild = self.        