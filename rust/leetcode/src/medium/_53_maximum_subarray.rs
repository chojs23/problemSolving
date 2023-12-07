//Greedy
//DP
struct Solution;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut dp = vec![0; nums.len() + 1];
        dp[0] = nums[0];
        let mut max = dp[0];

        for i in 1..nums.len() {
            dp[i] = nums[i].max(dp[i - 1] + nums[i]);
            max = max.max(dp[i]);
        }

        max
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::max_sub_array(vec![-2, 1, -3, 4, -1, 2, 1, -5, 4]),
        6
    );
    assert_eq!(Solution::max_sub_array(vec![1]), 1);
    assert_eq!(Solution::max_sub_array(vec![0]), 0);
    assert_eq!(Solution::max_sub_array(vec![-1]), -1);
    assert_eq!(Solution::max_sub_array(vec![-2147483647]), -2147483647);
}
