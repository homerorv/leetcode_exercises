'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4660/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

'''
 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        return slow


sol = Solution()
li = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,)))))
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
res = sol.middleNode(li)

print(res.val)







