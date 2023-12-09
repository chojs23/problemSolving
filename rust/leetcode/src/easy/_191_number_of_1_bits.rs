//Bit manupulation

struct Solution;
impl Solution {
    pub fn hammingWeight(n: u32) -> i32 {
        let mut count = 0;
        let mut n = n;
        while n != 0 {
            count += n & 1;
            n >>= 1;
        }

        count as i32
    }
}
