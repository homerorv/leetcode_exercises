'''
https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

100
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p== None or q==None:
            return False
        
        if p.val != q.val:
            result = False
        else:
            result = True
        left_result = self.isSameTree(p.left,q.left)
        right_result = self.isSameTree(p.right,q.right)
        return left_result and right_result and result

root = TreeNode(1,None)
left = TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7)))
right = TreeNode(3,None,TreeNode(8,TreeNode(9),None))
root.left =left
root.right = right

root_2 = TreeNode(1,None)
left_2 = TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7)))
right_2 = TreeNode(3,None,TreeNode(8,TreeNode(9)))
root_2.left =left_2
root_2.right = right_2

sol = Solution()

res = sol.isSameTree(root,root_2)
#Output: [1,2,3,4,5,8,6,7,9]
print("Is Same Tree:\t",res)