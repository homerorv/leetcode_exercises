'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        
        left = self.inorderTraversal_recursive(root.left)
        res.append(root.val)
        right = self.inorderTraversal_recursive(root.right)
        return left + res + right
        
    def inorderTraversal_interactive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        stack = [] 
        node = root
        while len(stack) > 0 or node != None:
            if node != None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right            
        return res



root = TreeNode(1,None)
left = TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7)))
right = TreeNode(3,None,TreeNode(8,TreeNode(9),None))
root.left =left
root.right = right

sol = Solution()
res = sol.inorderTraversal_recursive(root)
#Output: [4,2,6,5,7,1,3,9,8]
print("Recursive :\t",res)
res = sol.inorderTraversal_interactive(root)
print("Interactive :\t", res)
