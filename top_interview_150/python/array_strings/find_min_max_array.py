'''
Consider finding the problem of finding the minimum and the maximum elements in an array of n numbers.
 (a) Describe the input and the output. 
 (b) Design a divide and conquer algorithm
 (c) Let T(n) be the recurrence relation that represents the running of your algorithm. Give its formula. (d) Solve T(n).
'''
class item:
    def __init__(self,min,max):
        self.min = min
        self.max = max

class Solution_max_min:
    def max_min(self, nums: List[int], l:int, r:int)->item:
        if l == r:   #just 1 element in the array
            return item(nums[l],nums[l])
        if l+1 == r: #just 2 elements in the array
            if nums[l] > nums[r]: 
                return item(nums[r],nums[l])               
            else:
                return item(nums[l],nums[r])                 
        
        mid = (l+r) // 2
        left_item = self.max_min(nums,l,mid)
        right_item = self.max_min(nums,mid+1,r)

        final_min = min(left_item.min, right_item.min)
        final_max = max(left_item.max, right_item.max)
        return item(final_min,final_max)

nums = [4,0,1]    
sol = Solution_max_min()
res = sol.max_min(nums,0,len(nums)-1)
print("min: ", res.min)
print("max: ", res.max)