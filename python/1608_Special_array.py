"""You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.


Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000"""
from typing import List


class Solution:
    """
    T-O (max(n))
    S-O (max(n))
    """
    def specialArray(self, nums: List[int]) -> int:
        max_val = max(nums)
        num_counter = []
        while max_val >= -1:
            for i in nums:
                if i >= max_val:
                    num_counter.append(i)
            if len(num_counter) == max_val:
                return max_val
            else:
                max_val -= 1
                num_counter = []
        return -1


class Solution1:
    """
    T-O (n log(n))
    S-O (log(n))

    TODO: use bi_search in sorted array
    """
    def specialArray(self, nums: List[int]) -> int:
        for indx, num in enumerate(sorted(nums)):
            prev = -1 if indx == 0 else sorted(nums)[indx -1]
            next = sorted(nums)[indx]
            if prev < len(nums) - indx <= next:
                return len(nums) - indx
        return -1


for sol in (Solution, Solution1):
    assert sol().specialArray([3, 5]) == 2
    assert sol().specialArray([0, 0]) == -1
    assert sol().specialArray([0, 4, 3, 0, 4]) == 3











