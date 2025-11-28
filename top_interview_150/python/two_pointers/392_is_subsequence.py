'''
392. Is Subsequence
https://leetcode.com/problems/is-subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True        
        n = len(s)
        j = 0        
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j==n:
                return True        
        return False
            
s = "ac"
t = "ahbgdc"
sol = Solution()
res = sol.isSubsequence(s,t)
print(res)

