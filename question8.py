def findErrorNums(nums):
    result = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            result.append(abs(num))
    
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)
            break
    
    return result
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
result = findErrorNums(nums)
print("Output:", result)
