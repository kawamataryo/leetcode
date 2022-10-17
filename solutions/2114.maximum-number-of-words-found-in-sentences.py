#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word_count = 0

        for sentence in sentences:
            max_word_count = max(len(sentence.split()), max_word_count)

        return max_word_count
# @lc code=end
