struct Solution;

impl Solution {
    pub fn find_min(num: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = num.len() - 1;

        while l < r {
            let mid = (l + r) / 2;

            if num[mid] > num[r] {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        num[l]
    }
}

#[test]
fn test() {
    assert_eq!(Solution::find_min(vec![3, 4, 5, 1, 2]), 1);
    assert_eq!(Solution::find_min(vec![4, 5, 6, 7, 0, 1, 2]), 0);
}
