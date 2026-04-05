
'''
 Maximum Number of Balloons
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4663/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
    Input: text = "nlaebolko"
    Output: 1
Example 2:
    Input: text = "loonbalxballpoon"
    Output: 2
Example 3:
    Input: text = "leetcode"
    Output: 0

    balloon
    b=1
    a=1
    l=2
    o=2
    n=1

'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic_str = {}
        for letter in text:            
            dic_str[letter] = dic_str.get(letter,0) + 1
        res = 0
        while True:
            dic_str['b'] = dic_str.get('b',0) -1
            dic_str['a'] = dic_str.get('a',0) -1
            dic_str['l'] = dic_str.get('l',0) -2
            dic_str['o'] = dic_str.get('o',0) -2
            dic_str['n'] = dic_str.get('n',0) -1
            if dic_str['b'] > -1 and  dic_str['a'] > -1 and dic_str['l'] > -1 and dic_str['o'] > -1 and dic_str['n'] > -1:
                res += 1
            else:
                break
        return res

#text = "nlaebolko"
#Output: 1

text = "loonbalxballpoon"
#Output: 2

sol = Solution()
res = sol.maxNumberOfBalloons(text)
print(res)