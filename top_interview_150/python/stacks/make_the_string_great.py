'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4611/

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:

    Input: s = "leEeetcode"
    Output: "leetcode"

Example 2:

    Input: s = "abBAcC"
    Output: ""

'''

class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0:
            return s
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack and s[i] != stack[-1] and s[i].lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
                

sol = Solution()
#input = "leEeetcode"
input = "abBAcC"
res = sol.makeGood(input)

print(res)