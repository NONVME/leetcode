"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space."""


class Solution:
    """
    T-O (p+s)
    S-O (uniq(p) + uniq(s))
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s: list[str] = s.split()
        main_dict = dict()
        if len(set(pattern)) != len(set(list_s)) or len(pattern) != len(list_s):
            return False
        for indx, letter in enumerate(pattern):
            if not main_dict.get(letter):
                main_dict[letter] = list_s[indx]
            else:
                if main_dict.get(letter) != list_s[indx]:
                    return False
        return True


assert Solution().wordPattern(pattern="abba", s="dog cat cat dog") == True
assert Solution().wordPattern(pattern="abba", s="dog cat cat fish") == False
assert Solution().wordPattern(pattern="aaaa", s="dog cat cat dog") == False
assert Solution().wordPattern(pattern="abba", s="dog dog dog dog") == False
assert Solution().wordPattern(pattern="aba", s="cat cat cat dog") == False
