# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]: # type:ignore
        # if not head: return head
        # cur = head.next # first
        # prev= head # prev
        # prevT = None # prev to prev
        # first = True # Changing head for the first iteration
        # while cur:
        #     tmp = cur.next # preserving next part of list before disconnecting pointers
        #     # Swapping
        #     cur.next = prev
        #     if prevT != None:
        #         prevT.next = cur
        #     prev.next = tmp

        #     # shifting all pointers
        #     if first: # changing head for first swap only
        #         head = cur
        #         first = False
        #     cur = tmp.next if tmp else None
        #     prevT = prev
        #     prev = tmp
        # return head

        # RECURSION
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node