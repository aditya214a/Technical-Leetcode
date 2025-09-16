# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # type:ignore
        if len(lists)<=1:
            return lists[0] if lists else None
        def merge(l1,l2):
            dummy = ListNode(0)
            hD = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    hD.next = l1
                    l1 = l1.next
                else:
                    hD.next = l2
                    l2 = l2.next
                hD = hD.next
            hD.next = l1 or l2
            return dummy.next
        li = merge(lists[0], lists[1])
        if len(lists) == 2:
            return li
        for i in range(2,len(lists)):
            li = merge(li, lists[i])


        return li