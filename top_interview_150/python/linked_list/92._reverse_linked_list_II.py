'''
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
               1,3,2,4,5
               1,3,4,2,5
               1,4,3,2,5
               
      Output: [1,4,3,2,5]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        node_left = head
        prev_node_left = head
        
        while index < left:
            prev_node_left = node_left
            node_left = node_left.next
            index += 1
        node_right = node_left

        while index < right:
            node_right = node_right.next
            index += 1

        node_right = node_right.next



        while node_left != node_right:
            current = node_left
            temp = node_right.next
            prev_node_left.next = current.next
            node_left = prev_node_left.next
            node_right.next =current
            current.next = temp
            node_right = current
        return head
    
    

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))

sol = Solution()
head = sol.reverseBetween(l1,2,4)

while(head != None):
    print(head.val)
    head = head.next

        


