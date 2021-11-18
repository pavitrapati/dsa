# Binary search algorithm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
arr=[1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr, 5))