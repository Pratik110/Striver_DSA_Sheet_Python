def merge_arr(arr,low,mid,high):
    left = low
    right = mid+1
    newArr = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            smaller = arr[left]
            left+=1
        else:
            smaller = arr[right]
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


def mergeSort(arr , low: int, high: int):
    if low == high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge_arr(arr,low,mid,high)
