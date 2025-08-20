# Problem Statement : You are given an array of strings strs. Group the anagrams together. Return the answer in any order.

# Examples :

# Input: strs = ["eat","tea","tan","ate","nat","bat"]  
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# Solution:

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))  

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

# Test Cases
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))





