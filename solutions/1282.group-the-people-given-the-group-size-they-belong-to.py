#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_hash = {}
        for i, num in enumerate(groupSizes):
            if num in group_hash:
                group_hash[num].append(i)
            else:
                group_hash[num] = [i]

        ans = []
        for k, v in group_hash.items():
            for _ in range(len(v) // k):
                group = []
                for _ in range(k):
                    group.append(v.pop())
                ans.append(group)
        return ans
# @lc code=end
