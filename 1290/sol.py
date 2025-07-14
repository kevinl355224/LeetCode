from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Number of nodes will not exceed 30.
        """
        current = head
        ans = 0
        while current:
            ans = (ans << 1) | current.val
            current = current.next
        return ans

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    head = [1,0,1]
    head = build_linked_list(head)
    print(sol.getDecimalValue(head))