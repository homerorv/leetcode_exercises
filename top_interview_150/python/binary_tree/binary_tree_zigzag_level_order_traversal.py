'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
                return []
        queue = deque()
        queue.append(root)
        result = []
        direction = 1 # 1 left, -1 right
        while queue:
            row = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if direction > 0:
                    row.append(node.val)
                else:
                    row.insert(0,node.val)               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            direction = direction * -1
            result.append(row)
        return result


root = TreeNode(3)
left = TreeNode(9)
right = TreeNode(20,TreeNode(15),TreeNode(7))

root.left =left
root.right = right

sol = Solution()
res = sol.zigzagLevelOrder(root)

print("deepestLeavesSum: ", res)