'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4629/

Reachable Nodes With Restrictions

Solution

There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.

Example 1:

    Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
    Output: 4
    Explanation: The diagram above shows the tree.
    We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.

Example 2:

    Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
    Output: 3
    Explanation: The diagram above shows the tree.
    We have that [0,5,6] are the only nodes that can be reached from node 0 without visiting a restricted node.

'''
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for (x,y) in edges:
            graph[x].append(y)
            graph[y].append(x)

        restricted_set = set()

        for r in restricted:
            restricted_set.add(r)
        
        seen = set()

        def dfs(curr_node):
            if curr_node in seen or curr_node in restricted_set:
                return
            seen.add(curr_node)
            for next_node in graph[curr_node]:
                # Only call dfs if not seen
                if not next_node in seen:
                    if dfs(next_node):
                        return
            return
        
        dfs(0)
        return len(seen)

#n = 7
#edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
#restricted = [4,5]
#Output: 4


n = 7
edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
restricted = [4,2,1]
#Output: 3


sol = Solution()
res = sol.reachableNodes(n,edges,restricted)
print(res)