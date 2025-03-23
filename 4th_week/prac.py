from structures import BinaryMinHeap

def bubblesort(nums):
    size = len(nums)
    for j in range(size-1, -1, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
    return nums

def selectionsort(nums):
    size = len(nums)
    for j in range(size-1):
        idx = j
        for i in range(j+1, size):
            if nums[idx] > nums[i]:
                idx = i
        nums[j], nums[idx] = nums[idx], nums[j]
    return nums

def insertionsort(nums):
    size = len(nums)
    if size == 1:
        return

    for j in range(1, size):
        for i in range(j, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                break

    return nums

def quicksort(arr, start, end):
    if start > end:
        return
    # i: pivot 보다 작은 수들의 마지막 index
    # j: pivot과 비교할 범위
    pivot = end

    i = start - 1

    for j in range(start, end):
        # arr[j]가 pivot보다 작으면 i를 1 증가시키고 arr[j]와 arr[i]의 위치를 바꿈
        if arr[j] < arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[pivot], arr[i+1] = arr[i+1], arr[pivot]
    quicksort(arr, start, i)
    quicksort(arr, i+2, end)
    return arr

def merge(arr1, arr2):
    result = []

    start1 = 0
    start2 = 0

    while start1 < len(arr1) and start2 < len(arr2):

        if arr1[start1] < arr2[start2]:
            result.append(arr1[start1])
            start1 += 1
        else:
            result.append(arr2[start2])
            start2 += 1

    if start1 >= len(arr1):
        result.extend(arr2[start2:])
    else:
        result.extend(arr1[start1:])

    return result

def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    return merge(mergesort(left), mergesort(right))

def heapsort(arr):
    heap = BinaryMinHeap()

    for n in arr:
        heap.insert(n)

    return [heap.extract() for _ in range(len(arr))]