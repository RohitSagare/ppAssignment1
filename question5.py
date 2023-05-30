def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Copy remaining elements from nums2 to nums1 if any
    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    return nums1
input_num1= input('Enter space seperated numbers').split()
nums1=[int(num) for num in input_num1]
m = int(input('Enter first integer'))
input_num2= input('Enter space seperated numbers').split()
nums2=[int(num) for num in input_num2]
n = int(input('Enter second integer'))
result = merge(nums1, m, nums2, n)
print("Output:", result)
