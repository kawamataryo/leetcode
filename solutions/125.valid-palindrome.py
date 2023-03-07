#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalize_s = re.sub(r"[^a-z0-9]", "", s.lower())
        first = 0
        last = len(normalize_s) - 1

        while first < last:
            if normalize_s[first] != normalize_s[last]:
                return False
            first += 1
            last -= 1

        return True
# @lc code=end
