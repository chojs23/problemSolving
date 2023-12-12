//Heap
use std::{cmp, collections::BinaryHeap};

struct Solution;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut max_heap = BinaryHeap::from(stones);

        while max_heap.len() > 1 {
            let a = max_heap.pop().unwrap();
            let b = max_heap.pop().unwrap();

            match cmp::Ord::cmp(&a, &b) {
                cmp::Ordering::Greater => max_heap.push(a - b),
                cmp::Ordering::Less => max_heap.push(b - a),
                cmp::Ordering::Equal => (),
            }
        }

        if max_heap.is_empty() {
            0
        } else {
            max_heap.pop().unwrap()
        }
    }
}

#[test]
fn test() {
    assert_eq!(Solution::last_stone_weight(vec![2, 7, 4, 1, 8, 1]), 1);
}
