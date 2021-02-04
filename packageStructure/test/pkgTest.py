import os
import sys
fPath = os.path.dirname(os.path.realpath(__file__))  #  path of current file
#  as body of code is one directory up from this test directory
sys.path.append(os.path.split(fPath[0]))
'''
# print(os.getcwd())  #  working directory - not necessarily file location
# print(os.path.realpath(__file__))  #  full file location
# print(os.path.split(sys.path[0]))  #  path file last value - not sure of use
# print(os.path.dirname(os.path.realpath(__file__)))  #  directory of current file
# print(os.path.split(fPath)[0])  #  up one directory level
'''




file = 'test.dat'

x = componentA(file)

y = componentB(x)

z = componentC(y)

def consistencyCheck:
    if z == something:
        return True
    else:
        return False
