'''
Contiguous Array

https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4845/

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
 
Example 1:
    Input: nums = [0,1]
    Output: 2
    Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
    Input: nums = [0,1,0]
    Output: 2
    Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:
    Input: nums = [0,1,1,1,1,1,0,0,0]
    Output: 6
    Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        dic[0] = -1
        ans = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in dic:
                ans = max(ans, i - dic[count])
            else:
                dic[count] = i
        
        return ans
    
#nums = [0,1,0]
#Output: 2

nums = [0,1,1,1,1,1,0,0,0]
#Output : 6

sol = Solution()
res = sol.findMaxLength(nums)
print(res)