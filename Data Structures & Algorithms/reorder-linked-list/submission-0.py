# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head,head

        #seperate into 2
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #make reverse list
        second = slow.next
        prev = slow.next = None
        while second:
             tmp = second.next
             second.next = prev
             prev = second
             second = tmp
        #merge
        first, sec = head, prev
        while sec and first:
            tmp1,tmp2 = first.next, sec.next
            first.next = sec
            sec.next = tmp1
            first = tmp1
            sec = tmp2
    