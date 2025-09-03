#Problem Statement : Suppose an array of length n sorted in ascending order is rotated between 1 and n times.


#Examples:
# [0,1,2,4,5,6,7] rotated once → [4,5,6,7,0,1,2]

# [0,1,2,4,5,6,7] rotated four times → [5,6,7,0,1,2,4]

# Input : nums = [3,4,5,1,2]
# Output : 1


#Solution:-

nums = [3,4,5,1,2]

left = 0

right = len(nums) - 1

while left < right:

    mid = (left+right)//2
    
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

print(nums[left])