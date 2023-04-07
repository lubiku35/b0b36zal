def polyEval(poly, x):
    output = 0
    power = 1
    if poly[-1] == 0:
        poly.pop(-1)
     
    if len(poly) == 1:
        return poly[0]
    else:
        output += poly[0]
        for i in range(len(poly) - 1):
            output += poly[i + 1] * (x ** power)
            power += 1
        return output
 
 
 
def polySum(poly1, poly2):
    if len(poly1) > len(poly2):
        arr = poly1
        for i in range(len(poly2)):
            arr[i] += poly2[i]
    elif len(poly1) < len(poly2):
        arr = poly2
        for i in range(len(poly1)):
            arr[i] += poly1[i]
    else:
        arr = poly1
        for i in range(len(poly2)):
            arr[i] += poly2[i]
 
    while arr[-1] == 0:
        arr.pop()
     
    return arr
 
def polyMultiply(poly1, poly2):
    lst = []
    for i in range(len(poly1) + len(poly2) -1):
        lst.append(0)
    for j in range(len(poly1)):
        multipler = j
        for k in range(len(poly2)):
            lst[multipler + k] += poly1[multipler] * poly2[k]
    return lst