'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false

'''

class Solution:
    def checkIfPangram_paco(self, sentence: str) -> bool:   
        setAlpha = set(sentence)
        for letter in "abcdefghijklmnopqrstvwxyz":
            if letter not in setAlpha:
                return False
        return True

    def checkIfPangram(self, sentence: str) -> bool:   
        # Add every letter of 'sentence' to hash set 'seen'.
        seen = set(sentence)        
        # If the size of 'seen' is 26, then 'sentence' is a pangram.
        return len(seen) == 26


sol = Solution()
input = "thequickbrownfoxjumpsoverthelazydog"
res = sol.checkIfPangram(input)
print("Is Pangram :",res)
        