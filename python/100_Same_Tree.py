from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not isinstance(p, TreeNode) or not isinstance(q, TreeNode):
            if p == q:
                return True
            else:
                return False
        if p.val == q.val:
            self.isSameTree(p.left, q.left)
        else:
            return False


p = TreeNode(1, TreeNode(1, 2, 3), TreeNode(1, 2, 3))
q = TreeNode(1, TreeNode(1, 2, 3), TreeNode(1, 2, 3))

p1 = TreeNode(1, 2, 3)
q1 = TreeNode(1, 2, 3)


sol = Solution()

sol.isSameTree(p=p, q=q)
