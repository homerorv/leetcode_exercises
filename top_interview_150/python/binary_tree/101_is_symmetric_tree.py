'''
https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

'''
from queue import Queue

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric_recursive(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def is_mirror(node1: Optional[TreeNode],node2: Optional[TreeNode]):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            result = node1.val == node2.val
            return result and is_mirror(node1.left,node2.right) and is_mirror(node1.right,node2.left)
        return is_mirror(root,root)

    def isSymmetric_interactive(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        queue = Queue()
        queue.put(root)
        queue.put(root)
        while not queue.empty():
            node_left = queue.get()
            node_right = queue.get()
            if node_left ==None and node_right == None:
                continue
            if node_left == None or node_right == None:
                return False     
            if node_left.val != node_right.val:
                return False
            queue.put(node_left.left)
            queue.put(node_right.right)
            queue.put(node_left.right)
            queue.put(node_right.left)
        return True

#Input: root = [1,2,2,3,4,4,3]

left = TreeNode(2,TreeNode(3),TreeNode(4))
right = TreeNode(2,TreeNode(4),TreeNode(3))
root = TreeNode(1)
root.left =left
root.right = right

sol = Solution()
res = sol.isSymmetric_interactive(root)
#Output: [1,2,2,3,4,4,3]
print("Is Symmetric Tree (interactive):",res)

res = sol.isSymmetric_recursive(root)
#Output: [1,2,2,3,4,4,3]
print("Is Symmetric Tree (recursive)  :",res)