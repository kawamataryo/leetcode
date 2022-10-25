#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1 = l2 = c1 = c2 = 0

        while l1 < len(word1) or l2 < len(word2):
            if l1 == len(word1) or l2 == len(word2):
                return False

            if word1[l1][c1] != word2[l2][c2]:
                return False

            c1+= 1
            c2+= 1
            if  not c1 < len(word1[l1]):
                l1 += 1
                c1 = 0

            if not c2 < len(word2[l2]):
                l2 += 1
                c2 = 0

        return True
# @lc code=end
