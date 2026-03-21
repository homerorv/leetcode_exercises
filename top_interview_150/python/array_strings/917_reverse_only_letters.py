'''
https://leetcode.com/problems/reverse-only-letters/description/

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr_chars = s.toChat
        left =0
        right = len(arr_chars)-1
        while left < right:
            while left < len(arr_chars) and not arr_chars[left].isalpha():
                left += 1
            while right > -1 and not arr_chars[right].isalpha():
                right -= 1  
            if left+1 >= len(arr_chars) or left >=right:
                break         
            temp = arr_chars[left]
            arr_chars[left] = arr_chars[right]
            arr_chars[right] = temp
            left += 1
            right -= 1
        return "".join(arr_chars)    

sol = Solution()
#input = "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"

input = "tNH95P=TV"
#Output: "VTP95H=Nt"

#input = "7_28"
#Output: "7_28"

res = sol.reverseOnlyLetters(input)
print("Result:",res)    