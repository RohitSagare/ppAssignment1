def removeElement(nums, val):
    count = 0
    for num in nums:
        if num != val:
            nums[count] = num
            count += 1
    return count
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
val=int(input('enter any integer val'))
result = removeElement(nums, val)
print(result)
print("nums=", nums)
