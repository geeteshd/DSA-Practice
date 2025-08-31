# Problem Statement : Given an integer array nums, find the subarray (contiguous) within an array that has the largest product, and return the product.

# Examples : 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product = 6

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: [0] is the max product, since [-2,-1] product = 2 but they are not adjacent.


# Solution :-
         
nums = [-2,0,-1]
n = len(nums)
prefix = 1
suffix = 1
result = []
result.append(nums[0])

for i in range(n):

    if prefix!=0:
        prefix = prefix * nums[i] 
    else:
        nums[i]

    
    if suffix!=0:
        suffix = suffix * nums[n-1-i]
    else:
        nums[n-1-i]
    result.append(prefix)
    result.append(suffix)


print(max(result))





