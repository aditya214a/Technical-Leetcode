
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## MY SOLUTION
        # n1=''
        # n2=''
        # h1, h2 = l1, l2

        # while h1:
        #     n1 = str(h1.val) + n1
        #     h1 = h1.next

        # while h2:
        #     n2 = str(h2.val) + n2
        #     h2 = h2.next
        # res = str(int(n1) + int(n2))

        # dummy = ListNode(0)
        # dHead = dummy
        # for i in res[::-1]:
        #     temp = ListNode(int(i))
        #     dHead.next = temp
        #     dHead = dHead.next

        # return dummy.next

        # Efficient SOLUTION
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next