'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

'''
class Solution:
    def isPalindrome_paco(self, str_pal: str) -> bool:
        clean_string = lambda s: "".join(c.lower() for c in s if c.isalnum())
        cleaned_str = clean_string(str_pal)
        n = len(cleaned_str)
        k = (n/2) + 1
        for i in range(n):
            if cleaned_str[i] != cleaned_str[(n-1)-i]:
                return False
            if n-i < n/2:
                break
        return True
    
    def isPalindrome_official(self, str_pal: str) -> bool:
        i =0
        j = len(str_pal)-1
        while i < j:
            while i<j and not str_pal[i].isalnum():
                i += 1
            while i<j and not str_pal[j].isalnum():
                j -= 1
            if str_pal[i].lower() != str_pal[j].lower():
                return False
            i += 1
            j -= 1
        return True    
    
#s = "A man, a plan, a canal: Panama"
s="Anita lava latina"
#s="race a car"
sol = Solution()
res = sol.isPalindrome_official(s)
print(res)







