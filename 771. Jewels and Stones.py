'''
771. Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".


By:shenqiti
2019/9/26

'''
from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jj = 0
        J_collect = Counter(J)
        S_collect = Counter(S)
        for each in J_collect:
            jj += S_collect[each]

        return jj

dd = Solution()
J = "aA"
S = "aAAbbbb"
result = dd.numJewelsInStones(J,S)
print(result)
