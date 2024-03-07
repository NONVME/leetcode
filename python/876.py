"""
https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=daily-question&envId=2024-03-07

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, array: list) -> "ListNode":
        if not array:
            return None
        return cls(array.pop(0), cls.from_list(array))


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# assert Solution().middleNode(ListNode.from_list([1, 2, 3, 4, 5])) == ListNode.from_list([3, 4, 5])
# assert Solution().middleNode(ListNode.from_list([1, 2, 3, 4, 5, 6])) == ListNode.from_list([4, 5, 6])
