//Array, Bit Manipulation

use std::collections;

struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut map = collections::HashMap::new();

        for num in nums {
            let count = map.entry(num).or_insert(0);
            *count += 1;
        }

        for (key, value) in map {
            if value == 1 {
                return key;
            }
        }

        0
    }

    pub fn single_number2(nums: Vec<i32>) -> i32 {
        let mut result = 0;

        for num in nums {
            result ^= num;
        }

        result
    }
}

// 0000
// 0001
// xor
// 0001
//
// 0001
// 0011
// xor
// 0010

#[test]
fn test() {
    assert_eq!(Solution::single_number(vec![2, 2, 1]), 1);
    assert_eq!(Solution::single_number(vec![4, 1, 2, 1, 2]), 4);
}
