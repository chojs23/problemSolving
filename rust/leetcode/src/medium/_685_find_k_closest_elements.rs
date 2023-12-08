//two-pointer
struct Solution;

impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let (mut l, mut r) = (0, arr.len() - 1);

        while r - l >= k as usize {
            if x - arr[l] <= arr[r] - x {
                r -= 1;
            } else {
                l += 1;
            }
        }

        arr[l..r + 1].to_vec()
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::find_closest_elements(vec![1, 2, 3, 4, 5], 4, 3),
        vec![1, 2, 3, 4]
    );
    assert_eq!(
        Solution::find_closest_elements(vec![1, 2, 3, 4, 5], 4, -1),
        vec![1, 2, 3, 4]
    );
}
