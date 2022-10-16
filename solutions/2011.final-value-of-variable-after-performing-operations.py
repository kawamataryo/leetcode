#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        finalValue = 0

        for op in operations:
            if "++" in op:
                finalValue+= 1
            elif "--" in op:
                finalValue-= 1

        return finalValue
# @lc code=end
