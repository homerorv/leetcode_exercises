'''
A binary tree's maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth_recursive(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right==None:
            return 1

        left_depth = self.max_depth_recursive(root.left)
        right_depth = self.max_depth_recursive(root.right) 

        return max(left_depth,right_depth) + 1

    def max_depth_interactive(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = []
        if stack is not None:
            stack.append((1,root))        
        depth=0

        while len(stack) > 0:
            current_depth,node = stack.pop()
            if node is not None:
                depth = max(depth,current_depth)
                stack.append((current_depth+1,node.left))
                stack.append((current_depth+1,node.right))            
        return depth


root = TreeNode(3,None)
left = TreeNode(9)
right = TreeNode(20,TreeNode(15),TreeNode(7))
root.left =left
root.right = right

sol = Solution()
res = sol.max_depth_recursive(root)
#Output: 3
print("Max Depth recursive :\t",res)

res = sol.max_depth_interactive(root)
#Output: 3
print("Max Depth interactive:\t",res)