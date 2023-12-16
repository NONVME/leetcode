"""
https://leetcode.com/problems/valid-anagram/?envType=daily-question&envId=2023-12-16

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import Counter


class Solution:
    """
    T-O(n)
    S-0(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        for letter in s:
            if letter in s_counter:
                s_counter[letter] += 1
            else:
                s_counter[letter] = 1
        for letter in t:
            if letter in s_counter:
                s_counter[letter] -= 1
                if s_counter[letter] == 0:
                    del s_counter[letter]
            else:
                return False
        return not s_counter

class Solution1:
    """
    T-O(n2)
    S-O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        for letter in t:
            try:
                s_list.remove(letter)
            except ValueError:
                return False
        return not s_list


class Solution2:
    """
    T-O(n)
    S-0(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_char = [0] * 26
        for i in range(len(s)):
            map_char[ord(s[i]) - ord("a")] += 1
            map_char[ord(t[i]) - ord("a")] -= 1
        for i in map_char:
            if i != 0:
                return False
        else:
            return True


class Solution3:
    """
    One line
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


for sol in Solution3, Solution2, Solution1, Solution:
    assert sol().isAnagram("anagram", "nagaram") == True
    assert sol().isAnagram("anagram", "nagaram") == True
    assert sol().isAnagram("rat", "cat") == False
