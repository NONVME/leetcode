'''
https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        my_list = []
        while head:
            my_list.append(head.val)
            head = head.next
    
        left, right = 0, len(my_list) - 1
        while left < right and my_list[left] == my_list[right]:
            left += 1
            right -= 1
        return left >= right
