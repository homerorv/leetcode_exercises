'''
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Exmple 1: 

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:

    Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

    Output: [4,2,6,5,7,1,3,9,8]


'''
#Definition for a binary tree node.
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = Queue()
        queue.put(root)
        result = []
        while not queue.empty():
            level_size = queue.qsize()
            level_result = []
            node= None
            for i in range(0,level_size):
                node = queue.get()
                level_result.append(node.val)
                if node.left != None:
                    queue.put(node.left)
                if node.right != None:
                    queue.put(node.right)
            result.append(level_result)
        return result
    
    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        result = []
        left_result = self.levelOrder_recursive(root.left)
        right_result = self.levelOrder_recursive(root.right)

        result.append(root.val)
        return left_result + result + right_result

        
    def levelOrder_paco(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = Queue()
        queue.put(root)
        result = []
        level_queue = Queue()
        while not queue.empty():
            node_result = []
            node= None
            while not queue.empty():
                node = queue.get()
                node_result.append(node.val)
                level_queue.put(node)

            result.append(node_result)

            while not level_queue.empty():
                node = level_queue.get()
                if node.left != None:
                    queue.put(node.left)
                if node.right != None:
                    queue.put(node.right)
        return result

root = TreeNode(1,None)
left = TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6),TreeNode(7)))
right = TreeNode(3,None,TreeNode(8,TreeNode(9),None))
root.left =left
root.right = right

sol = Solution()

res = sol.levelOrder_paco(root)
#Output: [1,2,3,4,5,8,6,7,9]
print("Level Order Paco:\t",res)

res = sol.levelOrder(root)
#Output: [1,2,3,4,5,8,6,7,9]
print("Level Order :\t\t",res)

res = sol.levelOrder_recursive(root)
#Output: [1,2,3,4,5,8,6,7,9]
print("Level Order Recursive :\t",res)