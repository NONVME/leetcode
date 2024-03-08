"""
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2024-03-08

You are given an array nums consisting of positive integers.
Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
The frequency of an element is the number of occurrences of that element in the array.

Example 1:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List
import unittest


class Solution:
    """
    T-O(n)
    S-O(n)
    """
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        max_f = max(hash_map.values())
        res = 0
        for i in hash_map.values():
            if i == max_f:
                res += i
        return res


class TestMaxFrequencyElements(unittest.TestCase):

    def test_example1(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]), 4)

    def test_example2(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([1, 2, 3, 4, 5]), 5)

    def test_example3(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([10, 12, 11, 9, 6, 19, 11]), 2)

    def test_single_element(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([1]), 1)

    def test_all_same_elements(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([1, 1, 1, 1, 1]), 5)

    def test_empty_list(self):
        sol = Solution()
        self.assertEqual(sol.maxFrequencyElements([]), 0)

if __name__ == '__main__':
    unittest.main()
