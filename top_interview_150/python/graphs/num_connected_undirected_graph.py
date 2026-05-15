'''
Number of Connected Components in an Undirected Graph

https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4670/

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:

    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

Example 2:

    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1

'''
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for (x,y) in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        total = 0  

        def dfs(node): 
            seen.add(node)                   
            for child in graph[node]:
                if child not in seen:                    
                    dfs(child)

        for node in range(n):
            if node not in seen: 
                total = total + 1      
                dfs(node)
                
        return total


n = 5
edges = [[0,1],[1,2],[3,4]]

#edges = [[0,1],[1,2],[2,3],[3,4]]

sol = Solution()
res = sol.countComponents(n,edges)
print(res)