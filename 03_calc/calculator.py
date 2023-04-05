"""
    lab: 03_calc
    author: @lubiku
"""
from math import sqrt
 
def addition(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    else: return x + y
 
def subtraction(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    else: return x - y
 
def multiplication(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    else: return x * y
 
def division(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    elif y == 0: raise ValueError('This operation is not supported for given input parameters')
    else: return x / y
 
def modulo(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    elif y == 0: raise ValueError('This operation is not supported for given input parameters')
    elif x < y or y <= 0: raise ValueError('This operation is not supported for given input parameters')
    else: return x % y
 
def secondPower(x):
    type_x = type(x)
 
    if type_x == str: raise ValueError('This operation is not supported for given input parameters')
    else: return pow(x, 2)
 
def power(x, y):
    type_x = type(x)
    type_y = type(y)
 
    if type_x == str or type_y == str: raise ValueError('This operation is not supported for given input parameters')
    elif y < 0: raise ValueError('This operation is not supported for given input parameters')
    else: return float(x ** y)
 
def secondRadix(x):
    type_x = type(x)
 
    if type_x == str: raise ValueError('This operation is not supported for given input parameters')
    elif x <= 0: raise ValueError('This operation is not supported for given input parameters')
    else: return sqrt(x)
 
def magic(x, y, z, k):
    type_x = type(x)
    type_y = type(y)
    type_z = type(z)
    type_k = type(k)
 
    if type_x == str or type_y == str or type_k == str or type_z == str: raise ValueError('This operation is not supported for given input parameters')
    else:
        l = x + k
        m = y + z
        if m == 0: raise ValueError('This operation is not supported for given input parameters')
        else:
            n = ((l / m) + 1)
            return n    
 
def control(a, x, y, z, k):
 
    if a == 'ADDITION': return addition(x, y)
    elif a == 'SUBTRACTION': return subtraction(x, y)
    elif a == 'MULTIPLICATION': return multiplication(x, y)
    elif a == 'DIVISION': return division(x, y)
    elif a == 'MOD': return modulo(x, y)
    elif a == 'SECONDPOWER': return secondPower(x)
    elif a == 'POWER': return power(x, y)
    elif a == 'SECONDRADIX': return secondRadix(x)
    elif a == 'MAGIC': return magic(x, y, z, k)
    else: raise ValueError('This operation is not supported for given input parameters')