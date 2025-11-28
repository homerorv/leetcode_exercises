'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''



from typing import List

class Solution:
    def minSubArrayLen_paco(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sub_total = 0
        res_list = []
        for i in range(n):
            sub_total = nums[i]
            if sub_total >= target:
                res_list.append(1) 
                sub_total = 0
                continue
            for j in range(i+1,n):                
                sub_total += nums[j]            
                if sub_total >= target:
                    res_list.append((j-i)+1) 
                    sub_total = 0           
                    break
        if len(res_list) == 0:
            return 0
        else:
            return min(res_list)       

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        sub_total = 0        
        min_sub_array = float('inf')
        for right in range(n):
            sub_total += nums[right]                                                              
            while sub_total >= target:
                min_sub_array = min(min_sub_array, right - left + 1)                
                sub_total -= nums[left]
                left +=1

        if min_sub_array == float('inf'):
            return 0
        return min_sub_array


#target = 7
#nums = [2,3,1,2,4,3]
# expected out : 2, because 4,3

#target = 4
#nums = [1,4,4]
# expected Output: 1

#target = 11
#nums = [1,1,1,1,1,1,1,1]
# expected 0

target = 11
nums = [1,2,3,4,5]
# expected 3, because 3,4,5

sol = Solution()
res = sol.minSubArrayLen(target,nums)
print(res)

