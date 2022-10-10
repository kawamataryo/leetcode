/*
 * @lc app=leetcode id=20 lang=typescript
 *
 * [20] Valid Parentheses
 */

// @lc code=start
function isValid(s: string): boolean {
  const brackets = {
    "(": ")",
    "{": "}",
    "[": "]",
  }

  const stack: string[] = []

  for(let i = 0; i < s.length; i++ ){
    if(brackets[s[i]]) {
      stack.push(brackets[s[i]])
    } else if (stack && s[i] === stack[stack.length - 1]) {
      stack.pop()
    } else {
      return false
    }
  }
  console.log(stack.length)

  return stack.length === 0
};
// @lc code=end
