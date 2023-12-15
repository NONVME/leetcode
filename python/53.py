"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List

class Solution:
    """
    T-O(n)
    S-O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = largest_sum = nums[0]
        for i in range(1, len(nums)):
            i = nums[i]
            if i >= 0:
                if current_sum < 0:
                    current_sum = i
                else:
                    current_sum += i
            else:
                if current_sum < 0:
                    if current_sum < i:
                        current_sum = i
                else:
                    if current_sum > -i:
                        current_sum += i
                    else:
                        current_sum = 0

            if current_sum > largest_sum:
                largest_sum = current_sum
        return largest_sum if largest_sum > current_sum else current_sum


assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert Solution().maxSubArray([1]) == 1
assert Solution().maxSubArray([5,4,-1,7,8]) == 23
assert Solution().maxSubArray([-1]) == -1
assert Solution().maxSubArray([-3, -1]) == -1
assert Solution().maxSubArray([1, -1, 1]) == 1
assert Solution().maxSubArray([8,-19,5,-4,20]) == 21
