'''
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:

    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxlength=0
        def get_maxlength(node : Optional[TreeNode]):        
            if not node:
                return -1
            if node.left == None and node.right == None:
                return 0
            left_len = get_maxlength(node.left)
            right_len = get_maxlength(node.right)
            
            self.maxlength = max(self.maxlength,left_len+right_len+2) 
            node_length= max(left_len,right_len)+1
            return node_length
        get_maxlength(root)
        return self.maxlength

root = TreeNode(1)
left = TreeNode(2,TreeNode(4),TreeNode(5))
right = TreeNode(3)

# root = TreeNode(1)
# left = TreeNode(2)
# right = None

root.left =left
root.right = right

sol = Solution()
res = sol.diameterOfBinaryTree(root)

print("diameterOfBinaryTree: ", res)