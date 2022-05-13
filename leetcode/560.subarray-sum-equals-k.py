#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        res = 0

        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k

            res += hashmap[diff]
            hashmap[curSum] = 1 + hashmap[curSum]

        return res


# @lc code=end
