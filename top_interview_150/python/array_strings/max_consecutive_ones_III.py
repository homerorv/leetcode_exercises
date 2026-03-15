'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/

Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = res = num_0 = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_0 += 1
            while num_0 > k:
                if nums[left] == 0:
                    num_0 -= 1
                left += 1

            res = max(res,(right-left + 1))
        return res
    

sol = Solution()

input = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
#output 6
res = sol.longestOnes(input,k)
print("Result:",res)

input = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
#output 6\10
res = sol.longestOnes(input,k)
print("Result:",res)