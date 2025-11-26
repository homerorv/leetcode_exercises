'''
189. Rotate Array
https://leetcode.com/problems/rotate-array

Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''
class Solution:
    def rotate_using_other_array(self, nums: List[int], k: int) -> None:    
        n = len(nums)
        new_nums = [0]*n                
        for i in range(n):            
            new_nums[(i+k)%n] = nums[i]
        nums[0:] = new_nums[0:]

    def rotate_cyclic(self, nums: List[int], k: int) -> None:      
        n = len(nums)
        widx =k%n
        count =0
        start =0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + widx)%n
                aux = nums[next_idx]          
                nums[next_idx]=prev
                prev = aux
                current = next_idx
                count += 1
                if start == current:
                    break
            start +=1

nums =  [1,2,3,4,5,6,7]    
k = 3

#nums =  [-1,-100,3,99]        
#k = 2

sol = Solution()
sol.rotate_cyclic(nums,k)
print(nums)





