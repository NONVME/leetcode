"""
https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from functools import reduce
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for index, i in enumerate(nums):
            res.append(reduce(lambda x, y: x*y, nums[:index] + nums[index + 1:]))
        return res

class Solution1:
    """
    S-O(n)
    T-O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result



for sol in Solution1,:
    assert sol().productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert sol().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
