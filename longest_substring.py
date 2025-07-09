# Problem Statement : Given a string s, find the length of the longest substring without duplicate characters.

# Example 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Test Cases
print(length_of_longest_substring("abcabcbb")) 
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))   
print(length_of_longest_substring(""))          
print(length_of_longest_substring("au"))        
print(length_of_longest_substring("dvdf"))     

