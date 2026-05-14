'''
Find if Path Exists in Graph
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4693/

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:

    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2

Example 2:

    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.

'''
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = set()
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            seen.add(curr_node)
            for next_node in graph[curr_node]:
                # Only call dfs if not seen
                if not next_node in seen:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)


    def validPath_paco(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list) 
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()

        def dfs(source:int,target:int) -> bool:  
            if source == target:
                return True
            ans = False

            if source not in seen:
                seen.add(source)

            for node in graph[source]:
                if node not in seen:
                    ans = ans or dfs(node,target)
            return ans
        res = dfs(source,destination)
        return res

# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

n = 0
edges = []
source = 0
destination = 0


sol = Solution()
res = sol.validPath(n,edges,source,destination)
print(res)