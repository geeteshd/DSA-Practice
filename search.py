#  Problem Statement : You are given an integer array nums sorted in ascending order (with distinct values), 
#  but rotated at an unknown pivot. Given a target value, return its index. If it is not found, return -1.


# Examples :
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


# Solution :


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
# nums = [4,5,6,7,0,1,2]
# target = 3

        left= 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            return -1


s = Solution()

#TestCases:

print(s.search([4,5,6,7,0,1,2],0))
print(s.search([4,5,6,7,0,1,2],3))