class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Reverse
        prev = None
        curr = head

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        rev_head = prev

        # If n == 1, remove the head of reversed list
        if n == 1:
            rev_head = rev_head.next
        else:
            curr_add = rev_head

            for _ in range(1, n - 1):
                curr_add = curr_add.next

            curr_add.next = curr_add.next.next

        # Reverse again
        prev = None
        curr = rev_head

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        return prev