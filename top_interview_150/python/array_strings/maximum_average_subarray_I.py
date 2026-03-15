'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        sum = 0
        for i in range(k):
            sum += nums[i]
        res = sum/k
        
        for i in range(k,len(nums)):
            sum += nums[i]
            sum -= nums[i-k]
            res = max(res,sum/k)
        return res

sol = Solution()
input = [1,12,-5,-6,50,3]
k = 4 
res = sol.findMaxAverage(input,k)
print("Result:",res)
