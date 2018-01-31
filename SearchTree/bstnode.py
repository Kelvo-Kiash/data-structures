class BST(object):
    """[summary]
    
    [description]
    """ 
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = BSTNode(data)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if data < node.key:
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    
    




class BSTNode(object):
    def __init__(self, data):
        self.data = data
        self.disconnect()
    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None

    