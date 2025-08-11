# Problem Statement:
# Given two strings s and t, return the minimum window in s which will contain all the characters in t.
# If there is no such window in s that covers all characters in t, return the empty string.


# Example:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"


#Solution:
def min_window(s, t):
    need = {}
    for char in t:
        if char in need:
            need[char] += 1
        else:
            need[char] = 1

    have = {}
    have_count = 0
    required = len(need)

    left = 0
    min_len = len(s) + 1
    min_start = 0

    for right in range(len(s)):
        char = s[right]
        if char in have:
            have[char] += 1
        else:
            have[char] = 1

        if char in need and have[char] == need[char]:
            have_count += 1

        while have_count == required:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                min_start = left

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                have_count -= 1
            left += 1

    if min_len == len(s) + 1:
        return ""
    else:
        return s[min_start:min_start + min_len]

# TestCase
print(min_window("ADOBECODEBANC", "ABC"))

