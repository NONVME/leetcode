"""
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # pairs = []
        # for h, index in enumerate(height):
        #     pairs.append((h, index))
        # pairs.sort(key=lambda x: x[1], reverse=True)
        # res = 0
        # print(f"{pairs=}")
        # for f_index in range(len(pairs) - 1):
        #     print(f"{f_index=}")
        #     for s_index in range(f_index + 1, len(pairs)):
        #         # print(f"{s_index=}")
        #         width = abs(pairs[s_index][0] - pairs[f_index][0])
        #         height_ = min(pairs[s_index][1], pairs[f_index][1])
        #         res = max(width * height_, res)
        #         # print(f"{f_index=}, {s_index=}")
        #         print(f"{pairs[f_index]=}, {pairs[s_index]=}, {width=}, {height_=}, {res=}")
        # return res
        """
        T-O(n)
        S-O(1)
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 1]) == 1
assert Solution().maxArea([1, 2]) == 1
