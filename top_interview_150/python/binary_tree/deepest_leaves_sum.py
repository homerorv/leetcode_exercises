'''
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        #total_max_row = float("-inf")
        while queue:
            max_row = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                max_row += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)                                         
        return max_row

root = TreeNode(1)
left = TreeNode(2,TreeNode(4, TreeNode(7)),TreeNode(5))
right = TreeNode(3,None, TreeNode(6,None,TreeNode(8)))

root.left =left
root.right = right

sol = Solution()
res = sol.deepestLeavesSum(root)

print("deepestLeavesSum: ", res)
