struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();

        if chars.is_empty() {
            return true;
        }

        let mut i = 0;
        let mut j = chars.len() - 1;

        while i < j {
            if chars[i] != chars[j] {
                return false;
            }

            i += 1;
            j -= 1;
        }

        true
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::is_palindrome("A man, a plan, a canal: Panama".to_string()),
        true
    )
}
