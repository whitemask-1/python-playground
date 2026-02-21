# the leetcode problem was essentially take two singly linked lists and return a linked list with the sum of the two numbers
# However these singly linked lists digits are stored in reverse order

# For Example
# [3, 4, 1] = l1
# [5, 1, 3] = l2
# [8, 5, 4] = result


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    # first we need to set the dummy pointer which will point to whichever the last number added is (next)
    # however first it needs to start at 0 of a new list
    # also this list will store the result so we add the result variable

    result = dummy = ListNode()

    # Now how do we do math?
    # First we need to grab the frontmost value in the list and the add it to the total variable for that loop
    # Then after gathering the total for the current most foremost indexes of the two lists we find:

    total = carry = 0

    while (
        l1 or l2 or carry
    ):  # While there are any values in the lists or the carry count
        total = carry  # Set total equal to the carry upon reloop

        if l1:  # If theres a value in l1
            total += l1.val  # Add the value to the total
            l1 = l1.next  # Point to the next value in the list

        if l2:
            total += l2.val
            l2 = l2.next

        num = (
            total % 10
        )  #   - the number for dummy pointer and result list = total % 10 (remainder)
        carry = (
            total // 10
        )  #   - carry value = total // 10 (how many time 10 goes into total)
        dummy.next = ListNode(num)
        dummy = dummy.next

    return result.next
