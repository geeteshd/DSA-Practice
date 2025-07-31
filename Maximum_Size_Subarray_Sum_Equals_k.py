# Problem Statement: Given an array nums and an integer k, return the maximum length of a subarray that sums to k.


# Example: 
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation: Subarray [-1, 2] sums to 1.

#Solution:
def maxSubArrayLen(nums, k):
    prefix_sum = 0
    prefix_map = {}
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == k:
            max_len = i + 1

        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
    return max_len


#TestCases

print(maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(maxSubArrayLen([-2, -1, 2, 1], 1))
