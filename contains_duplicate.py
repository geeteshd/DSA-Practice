# Problem Statement : Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Solution:-

class Solution(object): 
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True  # Duplicate found within window

            seen.add(nums[i])

            # Maintain window size of at most k
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False

s = Solution()

#Test Cases

print(s.containsNearbyDuplicate([1, 2, 3, 1], 3)) 
print(s.containsNearbyDuplicate([1, 2, 3, 1], 2)) 
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1)) 
