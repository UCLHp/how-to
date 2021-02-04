file = 'test.dat'

x = componentA(file)

y = componentB(x)

z = componentC(y)

def consistencyCheck:
    if z == something:
        return True
    else:
        return False
