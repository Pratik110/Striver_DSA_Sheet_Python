from typing import *

def formPascalTriangleRow(rownum):
    res = 1
    arr = [res]
    for i in range(1,rownum):
        res = res * (rownum - i)
        res = res // i
        arr.append(res)
    return arr

# print(formPascalTriangleRow(2))

def pascalTriangle(n : int) -> List[List[int]]:
    resultArr = []
    # Write your code here.
    for i in range(1,n+1):
        rowArr = formPascalTriangleRow(i)
        resultArr.append(rowArr)
    # for row in resultArr:
    #     print(row)
    return resultArr

print(pascalTriangle(6))