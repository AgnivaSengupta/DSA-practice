#The target is to find the common Longest prefix in a grp of strings.
# Example:
# 
# "abcdabbb"  -->  "abcdabbb"  -->  "abcdabbb"  -->  "abcdabbb"
#  |                 |                 |                 |
# 
# "abcxzy"  -->  "abcxzy"  -->  "abcxzy"  -->  "abcxzy"
#  |               |               |               |
# 
# "abcccccccc" -->  "abcccccccc" -->  "abcccccccc" -->  "abcccccccc"
#  |                  |                  |                  |
# 
# Main idea is to traverse all the strings parallely and if any time the 
# equality is broken then return the string upto then

def longestCommPrefix(strs):
    if len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
    return strs[0]
    
strs = ["dog","racecar","car"]

print(longestCommPrefix(strs))

# =======================================================================================

#  Longest Substring Without Repeating Characters
# 
# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Optimal approach: Sliding window + last index

# Idea:
# Use two pointers forming a window [left, right]:
# Move right forward over the string.
# Maintain the last index of each character. --> a dictionary with the character as the key and index as the value
# If a character repeats inside the current window, move left to one position after the previous occurrence.
# Update the maximum window length at each step.
# This works in O(n) time.

def longestSubstringwithoutRepeat(str):
    if len(str) <= 1:
        return len(str)
    left = right = 0
    last = {}
    max_len = 0
    for right in range(len(str)):
        if str[right] in last and last[str[right]] >= left:
            left = last[str[right]] + 1
        last[str[right]] = right
        max_len = max(max_len, right - left+1)
    return max_len
        
print(longestSubstringwithoutRepeat("aua"))


# =======================================================================================================================
# 
# Longest Repeating Character Replacement:
# 
# given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# 
# Brute Force Approach:
# 