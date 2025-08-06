# Problem Statement: You are given a string s and an integer k.
# You can choose any character of the string and change it to any other uppercase letter, at most k times.

# Return the length of the longest substring containing the same letter after performing at most k character replacements.

# Example:
# Input: s = "ABAB", k = 2  
# Output: 4  
# Explanation: Replace both 'A's with 'B's or vice versa → "BBBB" or "AAAA"

# Input: s = "AABABBA", k = 1  
# Output: 4  
# Explanation: Replace one 'B' to get "AABA" or "ABAA"


#Solution

def characterReplacement(s, k):
    left = 0
    freq = {}
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1
        max_freq = max(max_freq, freq[char])

        if (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


#TestCases

print(characterReplacement("AABABBA", 1))
print(characterReplacement("ABAB", 2))
