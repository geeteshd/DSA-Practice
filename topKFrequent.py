# Problem Statement: Given an integer array nums and an integer k, return the k most frequent elements.
# You must solve it in O(n log n) or better O(n) time.

# # Examples:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]



# Solution:


nums = [1,1,1,2,2,3]
k = 2

count = {}

for i in nums:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

def get_frequency(item):
    return item[1] 

sorted_items = sorted(count.items(), key=get_frequency, reverse=True)

result = [item[0] for item in sorted_items[:k]]

print(result)
