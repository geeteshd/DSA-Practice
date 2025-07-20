# Problem Statement : Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

# Example : 

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # only start a sequence if it's the beginning of one
        if num - 1 not in num_set:
            current = num
            streak = 1

            while current + 1 in num_set:
                current += 1
                streak += 1

            longest = max(longest, streak)

    return longest


#Test Cases
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([1, 2, 0, 1]))
print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))



