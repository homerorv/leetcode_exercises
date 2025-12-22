'''
1. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists_paco(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        node1 = list1
        node2 = list2
        last = dummyHead
        while node1 != None or node2 != None:
            val1 = node1.val if node1 !=None else None
            val2 = node2.val if node2 !=None else None
            if val1 != None and val2 != None:
                if val1 < val2:
                    mergedVal = val1
                    node1 = node1.next
                else:
                    mergedVal = val2
                    node2 = node2.next                    
            else:
                if val2 == None: 
                    mergedVal = val1
                    node1 = node1.next
                else:
                    mergedVal = val2
                    node2 = node2.next                      
            new_node = ListNode(mergedVal)
            last.next = new_node
            last = last.next
            
        return dummyHead.next
    
    
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next    





#Input: l1 = [2,4,3], l2 = [5,6,4]
#output = Output: [7,0,8]
l1 = ListNode(1,ListNode(3,ListNode(5)))
l2 = ListNode(2,ListNode(4,ListNode(6,ListNode(8))))

sol = Solution()
head = sol.mergeTwoLists(l1,l2)

while(head != None):
    print(head.val)
    head = head.next



