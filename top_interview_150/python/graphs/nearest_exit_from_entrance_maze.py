'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4632/

Nearest Exit from Entrance in Maze

Solution
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:

    Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
    Output: 1
        Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
        Initially, you are at the entrance cell [1,2].
        - You can reach [1,0] by moving 2 steps left.
        - You can reach [0,2] by moving 1 step up.
        It is impossible to reach [2,3] from the entrance.
        Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:

    Input: `maze = `[["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
    Output: 2
        Explanation: There is 1 exit in this maze at [1,2].
        [1,0] does not count as an exit since it is the entrance cell.
        Initially, you are at the entrance cell [1,0].
        - You can reach [1,2] by moving 2 steps right.
        Thus, the nearest exit is [1,2], which is 2 steps away.

'''
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        def isValid(x,y):
            return (x>=0 and x<m) and (y<n and y>=0) and maze[x][y] == "."
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        seen = set()
        seen.add((entrance[0],entrance[1]))
        while queue:
            (x,y,d) = queue.popleft()
            if  (x,y) != (entrance[0],entrance[1]) and ((x == 0 or y ==0) or ( (x+1) == m or (y+1) == n )):
                return d
            
            for (inc_x,inc_y) in directions:
                new_x = x+inc_x
                new_y = y+inc_y
                if isValid(new_x,new_y) and not (new_x,new_y) in seen:
                    seen.add((new_x,new_y))
                    queue.append((new_x,new_y,d+1))
        return -1

maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

sol = Solution()
res = sol.nearestExit(maze,entrance)
print(res)

