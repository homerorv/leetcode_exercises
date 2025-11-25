'''
169. Majority Element
https://leetcode.com/problems/majority-element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)/2
        dic = {}
        dic[nums[0]] = 1
        for i in range(1,len(nums)):
            if dic.get(nums[i],None) != None:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for key in dic.keys():
            if dic[key] > maj:
                return key
        return None


nums = [2,2,1,1,1,2,2]
sol = Solution()
res = sol.majorityElement(nums)

print(res)