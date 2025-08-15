# # Problem Statement : Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# # Examples

# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False


# Solution:


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        have = {}
        need = {}
        
        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        for char in s:
            if char in have:
                have[char] += 1
            else:
                have[char] = 1

        return have == need

s = Solution()

# TestCases
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
