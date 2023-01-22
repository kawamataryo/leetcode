#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_dict = {}
        for bill in bills:
            if bill in bills_dict:
                bills_dict[bill] += 1
            else:
                bills_dict[bill] = 1

            if bill == 5:
                continue
            else:
                back = bill - 5
                while back:
                    if back >= 20 and 20 in bills_dict and bills_dict[20] > 0:
                        back -= 20
                        bills_dict[20] -= 1
                        continue
                    if back >= 10 and 10 in bills_dict and bills_dict[10] > 0:
                        back -= 10
                        bills_dict[10] -= 1
                        continue
                    if back >= 5 and 5 in bills_dict and bills_dict[5] > 0:
                        back -= 5
                        bills_dict[5] -= 1
                        continue
                    return False
        return True
# @lc code=end
