def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
target=int(input('enter target value'))
result = searchInsert(nums, target)
print("Output:", result)
