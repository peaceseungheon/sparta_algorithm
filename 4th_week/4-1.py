def sort(arr1, arr2):
    arr = arr1 + arr2
    return mergesort(arr)

def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[mid:]
    right = arr[:mid]

    return merge(mergesort(left), mergesort(right))


def merge(arr1, arr2):
    result = []

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    if i == len(arr1):
        result.extend(arr2[j:])
    else:
        result.extend(arr1[i:])

    return result