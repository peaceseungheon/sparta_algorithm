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
