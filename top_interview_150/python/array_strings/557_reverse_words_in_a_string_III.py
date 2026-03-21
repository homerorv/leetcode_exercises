'''
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0
        s_list = list(s)
        while left < len(s):
            while right < len(s) and s_list[right] != " ":
                right += 1
            temp_right = right -1
            while left < temp_right:
                temp = s_list[left]
                s_list[left] = s_list[temp_right]
                s_list[temp_right] = temp
                left += 1
                temp_right -= 1
            right += 1
            left = right
        return "".join(s_list)


    def reverseWords_2(self, s: str) -> str:
        array = s.split()
        for i in range(len(array)):
            array[i] = array[i][::-1]
        sol = " ".join(array)
        return sol

sol = Solution()
input = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
res = sol.reverseWords(input)
print("Result:",res)    