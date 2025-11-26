'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

'''
from typing import List


class Solution_paco:
    def removeElement(self, nums: List[int], val: int) -> int:
        w_idx=0
        r_idx=0
        if nums == None or len(nums) == 0:
            return 0
        if nums[0] != val:
            w_idx =1
        r_idx +=1
        while r_idx < len(nums):
            if nums[r_idx] != val:
                nums[w_idx] = nums[r_idx]
                w_idx += 1
            r_idx += 1
        return w_idx
    



class Solution_paco_not_good:
    def removeElement(self, nums: List[int], val: int) -> int:
        notequal = []
        for i in range(0,len(nums)):
            if nums[i]!=val:
                notequal.append(nums[i])
        for j in range(0,len(notequal)):
            nums[j] = notequal[j]
        return len(notequal)
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i



nums = [0,3,2,2,1,3]

val = 3

sol = Solution()
k = sol.removeElement(nums,val)
print("k:",k)
print("nums:",nums)



