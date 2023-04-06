from math import sin, cos
 
def newtonPi(init):
    if abs(init) == 2:
        for i in range(6):
            x = init - sin(init) / cos(init)
            init = x
    elif abs(init) == 3:
        for i in range(3):
            x = init - sin(init) / cos(init)
            init = x
    elif abs(init) == 4:
        for i in range(5):
            x = init - sin(init) / cos(init)
            init = x
    return x
 
 
def leibnizPi(iterations):
    X = 4
    operation = 1
    iterator = 1
    output = 0
 
    for i in range(iterations):
        output += operation * (X/iterator)
        operation *= -1
        iterator += 2
 
    return output
 
def nilakanthaPi(iterations):
    X = 4
    operation = 1
    iterator = 2
    output = float(3)
    if iterations > 1:
        for i in range(iterations - 1):
            output += operation * (X / (iterator * (iterator + 1) * (iterator + 2)))
            operation *= -1
            iterator += 2
 
    return output