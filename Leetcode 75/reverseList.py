'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
'''
Gist:
Use two pointers (prev and curr) to reverse links one node at a time.
Modify each node's next pointer to point to the previous node.
Continue until all nodes are reversed.

Time: O(N)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head  

        while curr:
            next_node = curr.next  
            curr.next = prev 
            prev = curr  
            curr = next_node  

        return prev