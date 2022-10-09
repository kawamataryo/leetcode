/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number) {
  // greedy
  // --------------------------------
  // for (let x = 0; x < nums.length; x++) {
  //   for (let y = x + 1; y < nums.length; y++) {
  //     if(target - nums[x] === nums[y]) {
  //       return [x, y]
  //     }
  //   }
  // }

  // two-hashmap
  // --------------------------------
  const hashmap: Record<string, number> = {}
  for (let i = 0; i < nums.length; i++) {
    hashmap[nums[i]] = i
  }
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i]
    if(hashmap[complement] && hashmap[complement] !== i) {
      return [hashmap[complement], i]
    }
  }
};
// @lc code=end
