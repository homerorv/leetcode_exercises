'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

    Input: root = [1,null,2,3]

    Output: [1,2,3]

Example 2:

    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

    Output: [1,2,4,5,6,7,3,8,9]

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        res.append(root.val)
        left = self.preorderTraversal_recursive(root.left)
        right = self.preorderTraversal_recursive(root.right)
        return res + left + right
        
    def preorderTraversal_interactive(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root == None:
            return res
        stack = []
        stack.append(root)
        while len(stack) > 0:
            item = stack.pop()
            res.append(item.val)
            if item.right != None:
                stack.append(item.right)
            if item.left != None:
                stack.append(item.left)
        return res



root = TreeNode(1,None)
left = TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7)))
right = TreeNode(3,None,TreeNode(8,TreeNode(9),None))
root.left =left
root.right = right

sol = Solution()
res = sol.preorderTraversal_recursive(root)
#Output: [1,2,4,5,6,7,3,8,9]
print(res)
res = sol.preorderTraversal_interactive(root)
print(res)