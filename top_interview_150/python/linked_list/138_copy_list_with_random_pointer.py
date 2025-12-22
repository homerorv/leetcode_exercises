'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer


A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.map = dict()

    def node_factory(self,current_old: 'Optional[Node]')->'Optional(Node)':
        if current_old == None:
            return None

        if current_old in self.map:
            new_current= self.map[current_old]
        else:
            new_current = Node(current_old.val,None,None)
            self.map[current_old] = new_current
        return new_current

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        dummy_head = Node(0,None,None)
        new_current = dummy_head
        while current != None:
            new_code = self.node_factory(current)
            new_code.random = self.node_factory(current.random)
            new_current.next = new_code
            new_current = new_current.next
            current = current.next
        return dummy_head.next

node1 = Node(1) 
node2 = Node(2)   
node3 = Node(3)     
node1.next = node2
node2.next = node3
node1.random = None
node2.random = node1
node3.random = node2

sol = Solution()

head = sol.copyRandomList(node1)

while(head != None):
    print(head.val," - ",head.random.val if head.random != None else None)
    head = head.next
