'''
Given the root of a binary tree, invert the tree, and return its root.
'''
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        new_left = self.invertTree_recursive(root.right)  
        new_right = self.invertTree_recursive(root.left)
        root.left = new_left
        root.right = new_right
        return root

    def invertTree_interactive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            level_size = queue.qsize()
            node= None
            for i in range(0,level_size):
                node = queue.get()
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left != None:
                    queue.put(node.left)
                if node.right != None:
                    queue.put(node.right)
        return root 


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
            

root = TreeNode(1,None)
left = TreeNode(2,TreeNode(4),TreeNode(5))
right = TreeNode(3,TreeNode(6),TreeNode(7))
root.left =left
root.right = right

sol = Solution()

res = sol.levelOrder(root)
print("Original Tree \t\t\t",res)
#Output: [1,[2,3],[4,5,6,7]

#inverted_root_interactive = sol.invertTree_interactive(root)
#res2 = sol.levelOrder(inverted_root_interactive)
#print("Inverted Tree Intertactive \t",res2)

inverted_root_recursive = sol.invertTree_recursive(root)
res2 = sol.levelOrder(inverted_root_recursive)
print("Inverted Tree Intertactive \t",res2)
