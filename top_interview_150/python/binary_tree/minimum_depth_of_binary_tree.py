'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 2

Example 2:

    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        if root.left == None:
            return self.minDepth(root.right) + 1
        
        if root.right == None:
            return self.minDepth(root.left) + 1

        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)

        res = min(min_left,min_right)+1

        return res

root = TreeNode(3)
left = TreeNode(9,TreeNode(3))
right = TreeNode(20,TreeNode(15),TreeNode(7,TreeNode(89)))
root.left =left
root.right = right

sol = Solution()
res = sol.minDepth(root)
#Output: 3
print("Min Depth recursive :\t",res)