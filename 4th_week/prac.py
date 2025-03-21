def bubblesort(nums):
    size = len(nums)
    for j in range(size-1, -1, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
    return nums