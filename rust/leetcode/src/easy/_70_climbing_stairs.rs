//DP

struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut dp = vec![0; n as usize + 2];
        dp[1] = 1;
        dp[2] = 2;

        for i in 3..=n as usize {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        dp[n as usize]
    }
}

#[test]
fn test() {
    assert_eq!(Solution::climb_stairs(2), 2);
    assert_eq!(Solution::climb_stairs(3), 3);
}
