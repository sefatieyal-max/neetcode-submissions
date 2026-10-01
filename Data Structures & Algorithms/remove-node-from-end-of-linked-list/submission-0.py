# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        #reverse the list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        #reverse and remove th n-th noed
        curr = prev
        prev = None
        while curr:
            n -= 1
            if n == 0:
                curr = curr.next
            else:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
        return prev

        

    

        