'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "(()[])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic_paren_def = {"(":")","[":"]","{":"}"}
        stack = []
        for letter in s:
            if letter in dic_paren_def.keys():
                # case open
                stack.append(letter)
            else:
                # case close
                if len(stack) == 0:
                    return False                
                close = stack.pop() 
                if letter != dic_paren_def.get(close):
                    return False
        return len(stack)==0
        

#Example 4:
s = "(()[])"
#Output: true

#Example 5:
#s = "])"
#Output: false

sol = Solution()
res= sol.isValid(s)

print(res)