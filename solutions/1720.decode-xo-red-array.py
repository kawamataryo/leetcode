#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])

        return result
# @lc code=end
