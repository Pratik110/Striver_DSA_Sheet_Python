from sys import *
from collections import *
from math import *

def printMatrix(matrix):
    for arr in matrix:
        print(arr)

def zeroMatrix(matrix, n, m):

    #Marking respective row/col array as 0 when we encounter any 0 in matrix
    col0Flag = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if j == 0:
                    col0Flag = 0
                else:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
    # printMatrix(matrix)
    # print(col0Flag)
    #Traversing [1,1] to [n,m] for marking entire row/col zero
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] != 0 and (matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
    # printMatrix(matrix)
    #Traversing col array
    for j in range(1,m):
        if matrix[0][j] != 0 and matrix[0][0] == 0:
            matrix[0][j] = 0
    #Traversing row array
    for i in range(n):
        if matrix[i][0] != 0 and col0Flag == 0:
            matrix[i][0] = 0
    # print(col0Flag)
    # printMatrix(matrix)
    return matrix

# matrix = [[1,1,1,1]
#         ,[1,0,1,1]
#         ,[1,1,0,1]
#         ,[0,1,1,1]]

matrix = [[2,4,3],[1,0,0]]
n = len(matrix)
m = len(matrix[0])

print(zeroMatrix(matrix, n, m))