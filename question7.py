def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    
    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
result = moveZeroes(nums)
print("Output:", result)
