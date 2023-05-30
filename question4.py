def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        sum = digits[i] + carry
        digits[i] = sum % 10
        carry = sum // 10
    
    if carry != 0:
        digits.insert(0, carry)
    
    return digits
input_num= input('Enter space seperated numbers').split()
nums=[int(num) for num in input_num]
result = plusOne(nums)
print("Output:", result)
