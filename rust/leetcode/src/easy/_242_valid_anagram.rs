struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_chars: Vec<char> = s.chars().collect();
        let mut t_chars: Vec<char> = t.chars().collect();

        s_chars.sort();
        t_chars.sort();

        s_chars == t_chars
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::is_anagram("anagram".to_string(), "nagaram".to_string(),),
        true
    );

    assert_eq!(
        Solution::is_anagram("rat".to_string(), "car".to_string()),
        false
    );
}
