# Problem Statement: Given a 1-indexed sorted array of integers numbers that is non-decreasing,
# find two numbers such that they add up to a specific target number.

# Examples: 
# Input: numbers = [2, 7, 11, 15], target = 9  
# Output: [1, 2]  
# Explanation: 2 + 7 = 9



# Solution: 


def twoSum(numbers, target):
    value_to_index = {}

    for i, num in enumerate(numbers):
        r = target - num

        if r in value_to_index:
            return [value_to_index[r] + 1, i + 1]

        value_to_index[num] = i

#TestCases

print(twoSum([-1, 0], -1))