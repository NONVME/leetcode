"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

class Solution:
    """
    T-O(n)
    S-O(n)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            else:
                set_nums.add(i)
        return False


class Solution1:
    """
    one line
    T-O(n)
    S-O(n)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False




for sol in Solution, Solution1:
    assert sol().containsDuplicate([1,2,3,1]) == True
    assert sol().containsDuplicate([1,2,3,4]) == False
    assert sol().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
