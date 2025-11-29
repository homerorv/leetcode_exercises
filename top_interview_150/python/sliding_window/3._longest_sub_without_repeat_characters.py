'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest substring without duplicate characters.


Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dict_count = dict()
        longest = 0
        #substring = []
        for right in range(len(s)):
            count = dict_count.get(s[right],0)
            dict_count[s[right]]=count+1
            while max(dict_count.values()) > 1:
                if dict_count[s[left]]>1:
                    dict_count[s[left]] = dict_count[s[left]] -1
                else:
                    del dict_count[s[left]]
                left += 1
            longest = max(longest,len(dict_count))
        return longest
    
#s = "abcabcbb"
# Expected  3

#s = "bbbbb"
# Output: 1

s = "pwwkew"
# Output: 1

sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print(res)


