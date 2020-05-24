class Node:
    def __int__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)


class Tree:
    def __int__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

