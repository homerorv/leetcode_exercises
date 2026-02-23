'''
Let us call an array sorted if it is sorted in a decreasing order. 
Consider the problem of checking whether a given array is unsorted order or not? Note that we do not ask for sorting the array.
 The solution should not involve sorting the array. Rather we want to check if it is sorted. 
 (a) Describe the problem formally, i.e., in the Input - Output format. 
 (b) What is the input size? 
 (c) What is the output size? 
 (d) Design a divide and conquer algorithm to solve the problem. 
 (e) Consider the following variant of the original problem: 
 Check if the odd indexed elements are sorted in an decreasing order. 
 Rewrite this new problem formally and design a divide and conquer algorithm to solve it.
'''


class Solution_isDescSorted:
    def is_sorted_desc(self, nums: List[int], left_idx:int, right_idx:int )->bool:

        if len(nums)<= 1: 
            return True

        if left_idx +1 == right_idx :   # left next to right
            if nums[left_idx] > nums[right_idx]:
                return True
            else:
                return False
        mid_idx = (left_idx + right_idx)//2            
        left_result = self.is_sorted_desc(nums,left_idx,mid_idx)
        right_result = self.is_sorted_desc(nums,mid_idx,right_idx)


        final_result = left_result and right_result
        return final_result


    def is_odd_sorted(self, nums: List[int], left_idx:int, right_idx:int )->bool:

        if left_idx == right_idx:
            return True

        if left_idx +1 == right_idx :   # left next to right
            return True 
            
        mid_idx = (left_idx + right_idx)//2       

        left_result = self.is_odd_sorted(nums,left_idx,mid_idx)
        right_result = self.is_odd_sorted(nums,mid_idx+1,right_idx)

        # ── Combine ─────────────────────────────────────────────
        # Last odd index in left half
        last_odd_left:   int = mid_idx     if mid_idx % 2 == 1       else mid_idx - 1
        # First odd index in right half
        first_odd_right: int = mid_idx + 1 if (mid_idx + 1) % 2 == 1 else mid_idx + 2

        boundary: bool
        if last_odd_left >= left_idx and first_odd_right <= right_idx:
            boundary = nums[last_odd_left] >= nums[first_odd_right]
        else:
            boundary = True 

        return left_result and right_result and boundary
    

nums = [100,10,100,9,100,8]    

sol = Solution_isDescSorted()
res = sol.is_odd_sorted(nums,0,len(nums)-1)

print("res: ", res)
