# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Edge case
        if not head or not head.next:
            return

        # --------------------------------
        # 1. Find the middle node
        # --------------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # --------------------------------
        # 2. Split the list
        # --------------------------------
        second = slow.next
        slow.next = None

        # --------------------------------
        # 3. Reverse the second half
        # --------------------------------
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # prev = head of reversed second half

        # --------------------------------
        # 4. Merge the two halves
        # --------------------------------
        first = head
        second = prev

        while second:
            # Save next nodes
            first_next = first.next
            second_next = second.next

            # Connect first -> second
            first.next = second

            # Connect second -> first_next
            second.next = first_next

            # Move forward
            first = first_next
            second = second_next