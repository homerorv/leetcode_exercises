'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, 
as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

'''

#Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root

    def printTree(self, root: Optional[TreeNode]):
        if root == None:
            return
        queue = deque()
        queue.append(root)
        while(queue):
            row = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                row.append(node.val)
            print(row)
        return



root = TreeNode(4)
left = TreeNode(2,TreeNode(1), TreeNode(3))
right = TreeNode(7)

root.left =left
root.right = right

sol = Solution()
new_root = sol.insertIntoBST(root,5)
res = sol.printTree(new_root)
