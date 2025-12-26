# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # already reversed
        prev = None

        # unprocessed
        curr = head

        while(curr):
            # store the next item in unprocest LList before we reverse it
            temp = curr.next
            
            # reverse current
            curr.next = prev

            # update previous
            prev = curr

            # return current pointer to unprocessed LList
            curr = temp

        return prev