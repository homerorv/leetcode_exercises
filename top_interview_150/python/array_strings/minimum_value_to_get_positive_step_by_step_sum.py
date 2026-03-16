'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4657/

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum

startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum_prefix = [nums[0]]
        for i in range(1,len(nums)):
            sum_prefix.append(nums[i]+sum_prefix[-1])
        
        value =1
        while (True):
            is_valid = True
            for j in range(0,len(sum_prefix)):
                if sum_prefix[j] + value < 1:
                    is_valid = False
                    break
            if is_valid :
                return value
            value +=1
        return -1
        
    def minStartValue_prefixsum(self, nums: List[int]) -> int:
        total = min_val = 0
        for i in range(0,len(nums)):
            total += nums[i]  
            min_val = min(total,min_val)  
        return -min_val+1
    

sol = Solution()
input = [-3,2,-3,4,2]
#Output: 5
res = sol.minStartValue(input)
print("Result:",res)

res = sol.minStartValue_prefixsum(input)
print("Result (prefix_sum):",res)
