'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m= len(grid)
        n= len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def isValid(row, col):
            if 0<= row and row < m and 0 <= col and col < n and grid[row][col] == 1:
                return True
            else:
                return False
            
        seen = set()
        
        def dfs(row,col)->int:
            total=0
            if grid[row][col] == 1 and (row,col) not in seen:
                total = 1
                seen.add((row,col))
                for (x,y) in directions:
                    next_x = row + x
                    next_y = col + y
                    if isValid(next_x,next_y) and (next_x,next_y) not in seen:
                        total+=dfs(next_x,next_y)
            return total
        
        max_val= 0
        for x in range(m):
            for y in range(n):
                if (x,y) not in seen:
                    total = dfs(x,y)
                    max_val= max(max_val,total)
        return max_val

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#output = 6

#grid = [[1,1,1],[0,0,0],[0,0,1]] 
#output = 3
sol = Solution()
res = sol.maxAreaOfIsland(grid)
print(res)