# Problem Statement: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example: Input: nums = [1,1,1], k = 2
#          Output: 2


# Solution: 

class Solution(object):
    def subarraySum(self,nums, k):
         count = 0
         current_sum = 0
         prefix_map = {0: 1}
         
         for num in nums:
              current_sum += num
              diff = current_sum - k
              if diff in prefix_map:
                  count += prefix_map[diff]
              prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
         return count

      
s = Solution()


#Test Cases

print(s.subarraySum([1,1,1],2))
print(s.subarraySum([1,2,3],3))