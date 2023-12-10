"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    T-O(n)
    S-O(1)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result: List[int] = []
        sL = len(s)
        pL = len(p)
        pattern = defaultdict(int)
        for i in p:
            pattern[i] += 1
        for index in range(sL):
            c_pattern = pattern.copy()
            for pattern_index in range(pL):
                if sL == index + pattern_index:
                    return result
                if (l :=s[index + pattern_index]) in c_pattern:
                    c_pattern[l] -= 1
                    if c_pattern[l] == 0:
                        c_pattern.pop(l)
                if not c_pattern:
                    result.append(index)
        return result

class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        # build hashmap
        for ch in p: hm[ch] += 1

        # initial full pass over the window
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
        # slide the window with stride 1
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm:
                hm[s[i+pL]] -= 1
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()):
                res.append(i+1)
        return res

for sol in Solution, Solution1:
    assert sol().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert sol().findAnagrams("abab", "ab") == [0, 1, 2]
    assert sol().findAnagrams("baa", "aa") == [1]
    assert sol().findAnagrams("acdcaeccde", "c") == [1, 3, 6, 7]
