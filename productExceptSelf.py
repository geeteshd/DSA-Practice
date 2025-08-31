# # Problem Statement : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Example: 

# Input:
# nums = [1,2,3,4]
# Output:
# [24,12,8,6]


# Solution:-


nums = [1,2,3,4]
n = len(nums)
result = [1] * n

prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n-1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

print(result)



    

