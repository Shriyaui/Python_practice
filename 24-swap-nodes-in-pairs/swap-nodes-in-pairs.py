# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to simplify handling the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse the list and swap pairs
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Swap the nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move to the next pair
            prev = first
        
        return dummy.next


# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to list for printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: [1,2,3,4]
    head1 = create_linked_list([1, 2, 3, 4])
    result1 = sol.swapPairs(head1)
    print("Input: [1,2,3,4]")
    print("Output:", linked_list_to_list(result1))
    print()
    
    # Test case 2: []
    head2 = create_linked_list([])
    result2 = sol.swapPairs(head2)
    print("Input: []")
    print("Output:", linked_list_to_list(result2))
    print()
    
    # Test case 3: [1]
    head3 = create_linked_list([1])
    result3 = sol.swapPairs(head3)
    print("Input: [1]")
    print("Output:", linked_list_to_list(result3))
    print()
    
    # Test case 4: [1,2,3]
    head4 = create_linked_list([1, 2, 3])
    result4 = sol.swapPairs(head4)
    print("Input: [1,2,3]")
    print("Output:", linked_list_to_list(result4))