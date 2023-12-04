struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = 1;

        let mut max = 0;

        while r < prices.len() {
            if prices[l] < prices[r] {
                max = max.max(prices[r] - prices[l]);
                r += 1;
            } else {
                l = r;
                r += 1;
            }
        }

        max
    }
}

#[test]
fn test() {
    assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
    assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
}
