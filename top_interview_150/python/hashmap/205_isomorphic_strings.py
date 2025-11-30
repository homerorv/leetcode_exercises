'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
 No two characters may map to the same character, but a character may map to itself.

 
Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Explanation:
    The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:

    Input: s = "foo", t = "bar"
    Output: false
    Explanation:
    The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

    Input: s = "paper", t = "title"

    Output: true

'''
class Solution:
    def isIsomorphic_paco(self, s: str, t: str) -> bool:
        dict_s_t = dict()
        dict_t_s = dict()
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]            
            if char_s not in dict_s_t:
                dict_s_t[char_s] = char_t
            else:
                if dict_s_t[char_s] != char_t:
                    return False
            
            if char_t not in dict_t_s:
                dict_t_s[char_t] = char_s
            else:
                if dict_t_s[char_t] != char_s:
                    return False                
        return True
    
    # Solution using First occurence transformation
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)



s = "paper"
t = "title"
#    Output: true

sol = Solution()
res = sol.isIsomorphic(s,t)
print(res)