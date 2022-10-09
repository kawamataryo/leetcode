/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
  // population solution
  // -------------------
  // if(x < 0) {
  //   return false
  // }

  // return x === Number(String(x).split("").reverse().join(""))

  // best solution
  // -------------------
  if(x < 0 || (x > 0 && x % 10 === 0)) {
    return false;
  }

  let result = 0
  while(x > result) {
    result = result * 10 + x % 10
    x = Math.floor(x / 10)
  }

  return result === x || Math.floor(result / 10) === x
};
// @lc code=end
