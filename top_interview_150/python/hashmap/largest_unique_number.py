'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/

Given an integer array nums, return the largest integer that only occurs once. 
If no integer occurs once, return -1.

Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.


Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.

'''

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        dic_nums = dict()
        for num in nums:
            dic_nums[num]= dic_nums.get(num,0)+1
        largest_nums = sorted(nums,reverse=True)    
        for num in largest_nums:
            if dic_nums[num] == 1:
                return num
        return -1
    

nums = [5,7,3,9,4,9,8,3,1]
#Output: 8

#nums = [9,9,8,8]
#Output: -1

#nums = [11,10,11]
#Output: 10

sol = Solution()
res = sol.largestUniqueNumber(nums)
print(res)



