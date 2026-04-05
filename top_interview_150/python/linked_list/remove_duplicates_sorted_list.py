'''
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

    Input: head = [1,1,2]
    Output: [1,2]

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = node
        while node and node.next:
            if  node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

sol = Solution()
li = ListNode(1,ListNode(1,ListNode(1))) 
#Input: head = [1,1,2]
#Output: [1,2]
res = sol.deleteDuplicates(li)

print(res.val)
