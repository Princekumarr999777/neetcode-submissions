# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        pointer_1=l1
        pointer_2=l2

        dummy=ListNode(-1)
        pointer_3=dummy
        carry=0
        while pointer_1:
           while pointer_1 or pointer_2 or carry:

            value_1 = pointer_1.val if pointer_1 else 0
            value_2 = pointer_2.val if pointer_2 else 0

            curr_value = value_1 + value_2 + carry

            digit = curr_value % 10
            carry = curr_value // 10

            pointer_3.next = ListNode(digit)

            pointer_3 = pointer_3.next

            if pointer_1:
                pointer_1 = pointer_1.next

            if pointer_2:
                pointer_2 = pointer_2.next

        return dummy.next

        