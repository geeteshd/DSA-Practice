def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

# Test cases
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))        
    print(two_sum([3, 2, 4], 6))             
    print(two_sum([3, 3], 6))                
