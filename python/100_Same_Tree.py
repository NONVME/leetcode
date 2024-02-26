"""
https://leetcode.com/problems/same-tree/description/?envType=daily-question&envId=2024-02-26

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}, {self.left}, {self.right}"


class Solution:
    """
    T-O(n)
    S-O(h)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#
#
# assert Solution().isSameTree(TreeNode(*[1, 2, 3]), TreeNode(*[1, 2, 3])) == True
# assert Solution().isSameTree(TreeNode(*[1, 2]), TreeNode(*[1, None, 2])) == False
# assert Solution().isSameTree(TreeNode(*[1, 2, 1]), TreeNode(*[1, 1, 2])) == False
#
# print(Solution().isSameTree(TreeNode(*[1, 2, 3]), TreeNode(*[1, 2, 3])))
