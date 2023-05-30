def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
result = containsDuplicate(nums)
print("Output:", result)
