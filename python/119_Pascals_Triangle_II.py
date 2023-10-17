from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [int(a) for a in str(11 ** rowIndex)]
