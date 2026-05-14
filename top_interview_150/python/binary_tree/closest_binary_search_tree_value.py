'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

Example 1:

    Input: root = [4,2,5,1,3], target = 3.714286
    Output: 4

Example 2:

    Input: root = [1], target = 4.428571
    Output: 1

'''
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return 0
        node = root
        close_val = node.val
        diff = abs(node.val-target)
        while node:
            diff_node= abs((node.val-target))
            if (diff_node < diff) or (diff_node == diff and node.val < close_val):
                close_val = node.val
                diff = diff_node
            if target < node.val:
                node = node.left
            elif target > node.val:
                node = node.right
            else:
                return node.val
        return close_val

    def closestValue_paco_search_all_tree(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return 0
        close_val = root.val
        diff = abs(root.val-target)
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            diff_node= abs((node.val-target))
            if (diff_node < diff) or (diff_node == diff and node.val < close_val):
                close_val = node.val
                diff = diff_node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return close_val

root = TreeNode(4)
left = TreeNode(2,TreeNode(1), TreeNode(3))
right = TreeNode(5)

root.left =left
root.right = right

sol = Solution()
res = sol.closestValue(root,3.7)
print("Closest item: ", res)