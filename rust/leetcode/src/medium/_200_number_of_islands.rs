//Graph-BFS
struct Solution;

impl Solution {
    const DIR: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let (max_r, max_c) = (grid.len(), grid[0].len());
        let mut visited = vec![vec![false; max_c]; max_r];

        let mut num = 0;

        for r in 0..max_r {
            for c in 0..max_c {
                if !visited[r][c] && grid[r][c] == '1' {
                    Self::bfs(r, c, &grid, &mut visited, &mut num);
                }
            }
        }

        num
    }

    fn bfs(r: usize, c: usize, grid: &[Vec<char>], visited: &mut [Vec<bool>], num: &mut i32) {
        let (max_r, max_c) = (grid.len(), grid[0].len());
        let mut queue = std::collections::VecDeque::<(i32, i32)>::with_capacity(r * c);
        queue.push_back((r as i32, c as i32));
        visited[r][c] = true;

        while !queue.is_empty() {
            let (r, c) = queue.pop_front().unwrap();

            for (dr, rc) in Self::DIR.iter() {
                let (nr, nc) = (r + dr, c + rc);

                if nr >= 0 && nr < max_r as i32 && nc >= 0 && nc < max_c as i32 {
                    if !visited[nr as usize][nc as usize] && grid[nr as usize][nc as usize] == '1' {
                        queue.push_back((nr, nc));
                        visited[nr as usize][nc as usize] = true;
                    }
                }
            }
        }

        *num += 1;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_200() {
        assert_eq!(
            Solution::num_islands(vec![
                vec!['1', '1', '1', '1', '0'],
                vec!['1', '1', '0', '1', '0'],
                vec!['1', '1', '0', '0', '0'],
                vec!['0', '0', '0', '0', '0']
            ]),
            1
        );
        assert_eq!(
            Solution::num_islands(vec![
                vec!['1', '1', '0', '0', '0'],
                vec!['1', '1', '0', '0', '0'],
                vec!['0', '0', '1', '0', '0'],
                vec!['0', '0', '0', '1', '1']
            ]),
            3
        );
    }
}
