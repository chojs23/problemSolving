//DP
struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![0; n + 2];
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return nums[0];
        }
        dp[1] = nums[0];
        dp[2] = nums[0].max(nums[1]);

        for i in 3..=n {
            dp[i] = dp[i - 1].max(dp[i - 2] + nums[i - 1]);
        }

        dp[n]
    }
}

#[test]
fn test() {
    assert_eq!(Solution::rob(vec![1, 2, 3, 1]), 4);
    assert_eq!(Solution::rob(vec![2, 7, 9, 3, 1]), 12);
}
