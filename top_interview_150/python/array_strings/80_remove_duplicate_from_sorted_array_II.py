'''
80. Remove Duplicates from Sorted Array II

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element 
appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in 
the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        widx=1
        i=1
        dup=1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                dup += 1
                if dup > 2:
                    i += 1
                    continue
            else:
                dup = 1
            nums[widx]=nums[i]
            widx += 1
            i += 1
        return widx
    
#nums = [1,1,1,2,2,3]
nums =  [0,0,1,1,1,1,2,3,3]
#nums =  [1,1]
sol = Solution()
result = sol.removeDuplicates(nums)
print(result)
print(nums)




