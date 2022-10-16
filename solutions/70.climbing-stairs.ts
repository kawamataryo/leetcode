/*
 * @lc app=leetcode id=70 lang=typescript
 *
 * [70] Climbing Stairs
 */

// @lc code=start
function climbStairs(n: number): number {
  const dp: number[] = [1, ...[...Array(n)].map(_ => 0)]

  for(let i = 0; i < n + 1; i++){
    dp[i] += (i >= 1 ? dp[i - 1] : 0)
    dp[i] += (i >= 2 ? dp[i - 2] : 0)
  }

  return dp[n]
};
// @lc code=end
