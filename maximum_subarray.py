# Problem Statement : Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

# Example: 

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSubArray(nums):
    current_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum

#TestCases
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))       
print(maxSubArray([5,4,-1,7,8]))
