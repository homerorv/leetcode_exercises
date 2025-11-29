'''
383. Ransom Note
https://leetcode.com/problems/ransom-note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''


import collections
from collections import Counter

class Solution:
    def canConstruct_two_dict(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = dict()
        dict_ransomNote = dict()
        for letter in magazine:
            dict_mag[letter] = dict_mag.get(letter,0) + 1
        for letter in ransomNote:
            dict_ransomNote[letter] = dict_ransomNote.get(letter,0) + 1 
        
        for letter,count in dict_ransomNote.items():
            if dict_mag.get(letter,0) < count:    
                return False
        return True

    def canConstruct_one_dict(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)        
        for letter in ransomNote:
            if counter.get(letter,None) != None:    
                counter[letter] -= 1    
            else:
                return False
            
            if counter[letter] < 0:
                return False
        return True    


ransomNote = "aabbb"
magazine = "aabbb"            
sol = Solution()
res = sol.canConstruct_one_dict(ransomNote,magazine)
print(res)