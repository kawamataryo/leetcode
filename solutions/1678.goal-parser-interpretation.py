#
# @lc app=leetcode id=1678 lang=python3
#
# [1678] Goal Parser Interpretation
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result.append('G')
            if command[i] == '(':
                i+=1
                sub_command = []
                while command[i] != ')':
                    sub_command.append(command[i])
                    i+=1
                if len(sub_command) == 0:
                    result.append('o')
                elif "".join(sub_command) == 'al':
                    result.append('al')
            i+=1
        return "".join(result)
# @lc code=end
