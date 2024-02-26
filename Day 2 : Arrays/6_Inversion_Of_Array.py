def merge_arr(arr,low,mid,high):
    left = low
    right = mid+1
    newArr = []
    cnt = 0
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            smaller = arr[left]
            left+=1
        else:
            smaller = arr[right]
            cnt += (mid - left + 1) 
            right+=1
        newArr.append(smaller)

    while left <= mid:
        newArr.append(arr[left])
        left+=1
    while right <= high:
        newArr.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i] = newArr[i-low]
    return cnt

def mergeSort(arr , low , high ):
    cnt = 0
    if low == high:
        return cnt
    mid = (low+high)//2
    cnt+=mergeSort(arr,low,mid)
    cnt+=mergeSort(arr,mid+1,high)
    cnt+=merge_arr(arr,low,mid,high)
    return cnt

arr = [3,2,1]
arr = [2, 5, 1, 3, 4]

arr = [52244275 ,123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162]
low = 0
high = len(arr) - 1
print(mergeSort(arr , low , high ))