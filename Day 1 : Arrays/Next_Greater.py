def nextGreater(arr):
    opArr = arr.copy()
    n = len(arr)
    stack = []
    stack.append(0)
    for i in range(1,n):
        stackTop = stack[-1]
        if arr[i] <= arr[stackTop]:
            stack.append(i)
        else:
            while stack and arr[i] > arr[stack[-1]]:
                idx = stack.pop()
                opArr[idx] = arr[i]
            stack.append(i)
    opArr[-1] = -1
    return opArr
