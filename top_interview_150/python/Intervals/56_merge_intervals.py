'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        # sort intervals. 
        intervals.sort(key= lambda x: x[0])
        merged = []
        last_index = 0
        merged.append(intervals[last_index])        
        for i in range(1,len(intervals)):
            if merged[last_index][1] >= intervals[i][0]: # verify if needs to merge.
                #merge
                merged[last_index][1] = max(intervals[i][1],merged[last_index][1]) 
            else:
                #not merge
                merged.append(intervals[i])
                last_index += 1
        return merged        
    
intervals = [[1,4],[2,3]]
# Output: [[1,4]]

#intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

#intervals = [[3,6],[1,3],[6,10],[11,18]]
# Output: [[1, 10], [11, 18]]

#intervals = [[1,4],[4,5]]
# Output: [[1,5]]

#intervals = [[4,7],[1,4]]
# Output: [[1,7]]

sol = Solution()
res = sol.merge(intervals)

print(res)


       
