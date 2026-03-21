'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4836/

You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
 
Example 1:

Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
              [7,11,14,23,24,]  
Output: [-1,-1,-1,5,4,4,-1,-1,-1]

5 = (7+4+3+9+1+8+5)//7 = 37//7 = 5.28 => 5
'''
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*len(nums) # Initize to the len ad to -1 all the elements.
        sub_sum = [nums[0]]
        for i in range(1,len(nums),1):
            sub_sum.append(nums[i]+sub_sum[len(sub_sum)-1])
        left = -1
        right = (k*2)
        for middle in range(k,len(nums)-k,1):
            if left < 0:
                res[middle] = (sub_sum[right])//((k*2)+1)
            else:
                res[middle] = (sub_sum[right]-sub_sum[left])//((k*2)+1)
            right += 1
            left += 1            
        return res


sol = Solution()
input = [7,4,3,9,1,8,5,2,6]
k = 3
#Output: [-1,-1,-1,5,4,4,-1,-1,-1]
res = sol.getAverages(input,k)
print("Result:",res)    