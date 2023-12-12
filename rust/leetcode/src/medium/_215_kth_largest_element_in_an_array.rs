//Heap
struct Solution;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut max_heap = std::collections::BinaryHeap::from(nums);

        for _ in 1..k {
            max_heap.pop();
        }

        max_heap.pop().unwrap()
    }
}

#[test]
fn test() {
    assert_eq!(Solution::find_kth_largest(vec![3, 2, 1, 5, 6, 4], 2), 5);
    assert_eq!(
        Solution::find_kth_largest(vec![3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        4
    );
}
