//Heap

struct Solution;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut points = points;
        points.sort_by(|a, b| {
            let a = a[0] * a[0] + a[1] * a[1];
            let b = b[0] * b[0] + b[1] * b[1];
            a.cmp(&b)
        });

        points[0..k as usize].to_vec()
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::k_closest(vec![vec![1, 3], vec![-2, 2]], 1),
        vec![vec![-2, 2]]
    );
    assert_eq!(
        Solution::k_closest(vec![vec![3, 3], vec![5, -1], vec![-2, 4]], 2),
        vec![vec![3, 3], vec![-2, 4]]
    );
}
