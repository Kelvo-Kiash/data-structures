from LinkedList.Node import Node

 class LinkedList(object);
    def __init__(self):
        self.head = None;
        self.counter = 0;

    #constant time 
    def insertStart(self, data);

    self.counter += 1;

        newNode = Node(data);
        if not self.head(data);
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;

    # constant time
    def size(self):
        return self.counter
    #insert at the end linear time 
    def insertEnd(self, data):
        newNode = Node(data);
        actualNode = self.head;

        while actualNode.nextNode is not None:
            actualNode = actualNode.newNode;
        
        actualNode.nextNode = newNode;

    #linear time or sub liear
    def remove(self, data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.newNode;
            else:
                self.head.remove(data, self.head)

    #linear time
    def traverseList(self):
        actualNode = self.head;

        while actualNode is not None;
        print("%s" % actualNode.data);
        actualNode = actualNode.nextNode;
