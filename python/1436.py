"""
https://leetcode.com/problems/destination-city/?envType=daily-question&envId=2023-12-15

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
"""
from typing import List

class Solution:
    """
    T-O(n)
    S-O(n)
    """
    def destCity(self, paths: List[List[str]]) -> str:
        path_map = {path[0]: path[1] for path in paths}
        def recursive_pointer(dirrection: str) -> str:
            if not path_map.get(dirrection):
                return dirrection
            else:
                return recursive_pointer(path_map[dirrection])
        return recursive_pointer(paths[0][1])


class Solution1:
    """
    T-O(n)
    S-O(n)
    """
    def destCity(self, paths: List[List[str]]) -> str:
        all_ = set ()
        for u, v in paths:
            all_.add(u)
            all_.add(v)
            for u, _ in paths:
                all_.discard(u)
        assert len(all_) == 1
        return all_.pop()


for sol in Solution1, Solution:
    assert sol().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo"
    assert sol().destCity([["B","C"],["D","B"],["C","A"]]) == "A"
    assert sol().destCity([["A","Z"]]) == "Z"

