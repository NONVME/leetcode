"""
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    """
    T-O(n3)
    S-O(1)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for first_indx, first in enumerate(nums):
            for second_indx, second in enumerate(nums):
                for third_indx, third in enumerate(nums):
                    if first_indx == second_indx or first_indx == third_indx or second_indx == third_indx:
                        continue
                    else:
                        sorted_triplet = sorted(list((first, second, third)))
                        if sum(sorted_triplet) == 0:
                            result.add(tuple(sorted_triplet))

        result = [list(x) for x in result]
        return list(result)


class Solution1:
    """
    T-O(n2)
    S-O(n)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       res = []
       nums.sort()

       for i in range(len(nums)):
           if i > 0 and nums[i] == nums[i-1]:
               continue
           
           j = i + 1
           k = len(nums) - 1

           while j < k:
               total = nums[i] + nums[j] + nums[k]
               if total > 0:
                   k -= 1
               elif total < 0:
                   j += 1
               else:
                   res.append([nums[i], nums[j], nums[k]])
                   j += 1
                   while nums[j] == nums[j-1] and j < k:
                       j += 1
        
       return res

for sol in (Solution, Solution1):
    assert sol().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert sol().threeSum([0, 1, 1]) == []
    assert sol().threeSum([0, 0, 0]) == [[0, 0, 0]]
