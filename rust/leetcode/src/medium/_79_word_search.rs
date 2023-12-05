//BackTracking

struct Solution;

impl Solution {
    const DIRS: [[i32; 2]; 4] = [[-1, 0], [1, 0], [0, 1], [0, -1]];

    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut visited = vec![vec![false; board[0].len()]; board.len()];

        for r in 0..board.len() {
            for c in 0..board[0].len() {
                if Self::dfs(&board, &word, r, c, 0, &mut visited) {
                    return true;
                }
            }
        }

        false
    }

    fn dfs(
        board: &Vec<Vec<char>>,
        word: &String,
        r: usize,
        c: usize,
        k: usize,
        visited: &mut Vec<Vec<bool>>,
    ) -> bool {
        if k == word.len() {
            return true;
        }

        if r >= board.len() || c >= board[0].len() || visited[r][c] {
            return false;
        }

        if board[r][c] != word.chars().nth(k).unwrap() {
            return false;
        }

        visited[r][c] = true;

        let mut result = false;

        for [dr, dc] in Self::DIRS {
            let r = r as i32 + dr;
            let c = c as i32 + dc;

            if r < 0 || c < 0 {
                continue;
            }

            let r = r as usize;
            let c = c as usize;

            if Self::dfs(board, word, r, c, k + 1, visited) {
                result = true;
                break;
            }
        }

        visited[r][c] = false;
        result
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::exist(
            vec![
                vec!['A', 'B', 'C', 'E'],
                vec!['S', 'F', 'C', 'S'],
                vec!['A', 'D', 'E', 'E']
            ],
            "ABCCED".to_string()
        ),
        true
    );
    assert_eq!(
        Solution::exist(
            vec![
                vec!['A', 'B', 'C', 'E'],
                vec!['S', 'F', 'C', 'S'],
                vec!['A', 'D', 'E', 'E']
            ],
            "SEE".to_string()
        ),
        true
    );
    assert_eq!(
        Solution::exist(
            vec![
                vec!['A', 'B', 'C', 'E'],
                vec!['S', 'F', 'C', 'S'],
                vec!['A', 'D', 'E', 'E']
            ],
            "ABCB".to_string()
        ),
        false
    );
}
