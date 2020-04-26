def catAndMouse(x, y, z):
    if(abs(z - x) < abs(z - y)):
        return("Cat A")
    if(abs(z - x) > abs(z - y)):
        return("Cat B")
    else:
        return("Mouse C")