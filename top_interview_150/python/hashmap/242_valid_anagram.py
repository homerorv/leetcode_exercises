'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

    Input: s = "anagram", t = "nagaram"

    Output: true

Example 2:

    Input: s = "rat", t = "car"

    Output: false
'''

import collections


class Solution:
    def isAnagram_paco(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram_with_dict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        for k,v in dict_s.items():
            val = dict_s.get(k,None)
            if val == None:
                return False
            if val != dict_t[k]:
                return False
        return True


s = "anagram"
t = "nagaram"

sol = Solution()
res = sol.isAnagram_with_dict(s,t)
print(res)
