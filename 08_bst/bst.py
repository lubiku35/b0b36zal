class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.visited = 0
     
    def insert(self, value):
        new_node = Node(value)
        if self.root is None: self.root = new_node
        else:
            current = self.root       
            while True:
                if value < current.value:
                    if current.left is None: 
                        current.left = new_node
                        return
                    else: current = current.left
                if value > current.value:
                    if current.right is None:
                        current.right = new_node
                        return
                    else: current = current.right
                 
 
    def fromArray(self, array):
        for item in array: self.insert(item)
 
    def search(self, value):
        self.visited = 0
        current = self.root
        while current is not None:
            if current.value == value:
                self.visited += 1
                return True
            else:
                if value < current.value: current = current.left
                else: current = current.right
                self.visited += 1
        return False
 
 
    def min(self):
        self.visited = 1
        current = self.root
        if current is not None:
            while current.left is not None:
                current = current.left
                self.visited += 1
            return current.value
        else:
            return None
 
 
    def max(self):
        self.visited = 1
        current = self.root
        if current is not None:
            while current.right is not None:
                current = current.right
                self.visited += 1
            return current.value
        else:
            return None
 
    def visitedNodes(self):
        return self.visited
 
 
bst3 = BinarySearchTree()
bst3.fromArray([1, 3, 4, 5, 6, 7, 8])
 
print('MIN: ' + str(bst3.min()))
print(bst3.visitedNodes())
print('MAX: ' + str(bst3.max()))
print(bst3.visitedNodes()) 
 
 
print()
print()
print()
 
bst2 = BinarySearchTree()
bst2.fromArray([5, 3, 1, 4, 7, 6, 8])
 
print(bst2.search(5))
print(bst2.visitedNodes())
print(bst2.search(7))
print(bst2.visitedNodes())
print(bst2.search(6))
print(bst2.visitedNodes())
print(bst2.search(10))
print(bst2.visitedNodes())
print('MIN: ' + str(bst2.min()))
print(bst2.visitedNodes())
print('MAX: ' + str(bst2.max()))
print(bst2.visitedNodes()) 