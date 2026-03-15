'''
https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

55. Jump Game
Medium

Topics
conpanies icon
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leftIndex = nums[0]-1        
        while leftIndex < len(nums):
            jump = nums[leftIndex]
            leftIndex += jump
            if leftIndex == len(nums)-1:
                return True
            if jump == 0:
                break
        return False


sol = Solution()
#input = [2,3,1,1,4]
# res = true

input = [3,2,1,0,4]
# res = false
res = sol.canJump(input)
print("Result :", res)




