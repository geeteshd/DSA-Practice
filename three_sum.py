class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
        # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move inward
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


s = Solution()

#Test Cases
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
