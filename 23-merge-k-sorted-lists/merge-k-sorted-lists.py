class Solution(object):
    def mergeKLists(self, lists):
        values = []

        # Collect all values
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next

        # Sort values
        values.sort()

        # Create merged linked list
        dummy = ListNode(0)
        current = dummy

        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next