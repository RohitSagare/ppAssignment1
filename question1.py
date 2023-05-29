def twoSum(nums, target):
    num_map = {} 
    for i, num in enumerate(nums):
        counter = target - num  

        if counter in num_map:
            return [num_map[counter], i]  

        num_map[num] = i  

    return []

input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
target=int(input('enter target value'))
result = twoSum(nums,target)
print(result)

