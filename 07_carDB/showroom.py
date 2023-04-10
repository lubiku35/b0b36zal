class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
 
class LinkedList:
    def __init__(self):
        self.head = None
 
class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
 
db = LinkedList()
 
def clean():
    db.head = None
 
def getDatabaseHead():
    return db.head
 
 
def getDatabase():
    return db
 
def calculateCarPrice():
    head_node = getDatabaseHead()
    price = 0
    while head_node is not None:
        if head_node.data.active:
            price += head_node.data.price
        head_node = head_node.nextNode
    return price
 
 
def add(car):
    new_node = Node(None, None, car)
    head_node = getDatabaseHead()
 
    if head_node is None:
        db.head = new_node
    elif car.price < head_node.data.price:
        new_node.nextNode = db.head
        db.head = new_node
        new_node.nextNode.prevNode = new_node
    else:
        while (head_node.nextNode is not None) and (head_node.nextNode.data.price <= car.price):
            head_node = head_node.nextNode
     
        new_node.nextNode = head_node.nextNode
        head_node.nextNode = new_node
        new_node.prevNode = head_node
 
        if head_node.nextNode is None:
            new_node.nextNode.prevNode = new_node
 
def init(cars):
    for car in cars:
        add(car)
 
def updateName(identification, name):
    head_node = getDatabaseHead()
    while (head_node is not None) and (identification != head_node.data.identification):
        head_node = head_node.nextNode
    if head_node is not None:
        head_node.data.name = name
 
def updateBrand(identification, brand):
    head_node = getDatabaseHead()
    while (head_node is not None) and (identification != head_node.data.identification):
        head_node = head_node.nextNode
    if head_node is not None:
        head_node.data.brand = brand
 
def deactivateCar(identification):
    head_node = getDatabaseHead()
    while (head_node is not None) and (identification != head_node.data.identification):
        head_node = head_node.nextNode
    if head_node is not None:
        head_node.data.active = False
 
 
def activateCar(identification):
    head_node = getDatabaseHead()
    while (head_node is not None) and (identification != head_node.data.identification):
        head_node = head_node.nextNode
    if head_node is not None:
        head_node.data.active = True