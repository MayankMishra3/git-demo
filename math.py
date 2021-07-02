
def add(x,y):
    return x+y
  
def subtract(x,y):
    return x-y     #on Bug456
  
def multiply(x,y):
    return x*y       #on master
  
def divide(x,y):
    if y == 0:
        return operation_invalid
    else:
        return x/y        #on bug789
