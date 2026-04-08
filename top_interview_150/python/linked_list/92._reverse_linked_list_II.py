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
        node = head
        prev = None


        # Move to the initial position 
        while index < left:
            prev = node
            node = node.next
            index += 1

        left_prev_head = prev
        right_tail = node        

        while index <= right:
            next_node  = node.next                
            node.next = prev
            prev = node                
            node = next_node                  
            index += 1

        if left_prev_head:
            left_prev_head.next = prev
        else:
            head = prev
        
        right_tail.next = node
        
        return head     

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))

sol = Solution()
head = sol.reverseBetween(l1,2,4)
# Output: [1,4,3,2,5]
while(head != None):
    print(head.val)
    head = head.next

        


