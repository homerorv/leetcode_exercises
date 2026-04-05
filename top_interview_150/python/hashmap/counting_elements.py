'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/

Counting Elements

Solution
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
If there are duplicates in arr, count them separately.


Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        set_arr = set(arr) 
        count = 0
        for i in arr:
            if (i+1) in set_arr:
                count += 1
        return count

sol = Solution()
input = [1,2,3]
#input = [1,1,3,3,5,5,7,7]

res = sol.countElements(input)
print("Count Elements: ",res)