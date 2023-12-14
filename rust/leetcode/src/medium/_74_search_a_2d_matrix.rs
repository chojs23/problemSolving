//Binary Search
struct Solution;

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let (r, c) = (matrix.len() as i32, matrix[0].len() as i32);
        let mut left = 0;
        let mut right = r * c - 1;

        while left <= right {
            let mid = (left + right) / 2;
            let mid_val = matrix[mid.div_euclid(c) as usize][mid.rem_euclid(c) as usize];
            match mid_val.cmp(&target) {
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Less => left = mid + 1,
                std::cmp::Ordering::Greater => right = mid - 1,
            }
        }

        false
    }
}

#[test]
fn test() {
    // assert_eq!(
    //     Solution::search_matrix(
    //         vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]],
    //         3
    //     ),
    //     true
    // );
    assert_eq!(Solution::search_matrix(vec![vec![1]], 0), false);
}
