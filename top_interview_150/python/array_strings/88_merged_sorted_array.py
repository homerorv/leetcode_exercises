'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside 
the array nums1. To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
'''

from typing import List

class Solution_paco:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1
        for idx in range(m+n-1,-1,-1):
            #aux = nums1[i] if nums1[i]>0 else nums2[j]
            if j>=0:
                if i>=0 and nums1[i]>nums2[j]:
                    nums1[idx] = nums1[i]
                    i -= 1
                else:
                    nums1[idx] = nums2[j]
                    j -= 1
            else:
                nums1[idx] = nums1[i]
                i -= 1
  

class Solution_official:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backward through the array, each time writing
        # the largest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


#nums1 = [1,2,3,4,6,0,0,0]
#m = 5
#nums2 = [5,7,8]
#n = 3

nums1 = [2,0]
m = 1
nums2 = [1]
n = 1


sol_paco = Solution_paco()
sol_paco.merge(nums1,m,nums2,n)
print(nums1)

#nums1 = [1,2,3,4,6,0,0,0]
nums1 = [2,0]
sol_official = Solution_official()
sol_official.merge(nums1,m,nums2,n)
print(nums1)