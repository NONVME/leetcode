"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    """
    T-O(n)
    S-O(n)
    """
    @staticmethod
    def is_b_closed(s: str) -> bool:
        stack = []
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for i in s:
            if i in pairs.values():
                stack.append(i)
            if i in pairs.keys():
                if stack and stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        return not stack


class Solution1:
    """
    T-O(n)
    S-O(n)
    """
    @staticmethod
    def is_b_closed(s: str) -> bool:
        counter_b = {
            "(":0,
            "[":0,
            "{":0,
        }
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for i in s:
            if i in pairs.values():
                counter_b[i] += 1
            if i in pairs.keys():
                counter_b[pairs[i]] -= 1
                if counter_b[pairs[i]] < 0:
                    return False
        return not sum(counter_b.values())


for sol in Solution1, Solution:
    assert sol.is_b_closed("[()]{}") == True
    assert sol.is_b_closed("[)]") == False
    assert sol.is_b_closed("}{") == False
    assert sol.is_b_closed("(()") == False
    # assert sol.is_b_closed("([)]") == False
