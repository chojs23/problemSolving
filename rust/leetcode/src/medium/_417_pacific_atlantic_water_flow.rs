//Graph-BFS
struct Solution;

const DIR: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (max_r, max_c) = (heights.len(), heights[0].len());

        let pacific = Self::bfs(
            &heights,
            (0..max_c as i32)
                .map(|c| (0, c))
                .chain((0..max_r as i32).map(|r| (r, 0)))
                .collect(),
        );

        let atlantic = Self::bfs(
            &heights,
            (0..max_c as i32)
                .map(|c| (max_r as i32 - 1, c))
                .chain((0..max_r as i32).map(|r| (r, max_c as i32 - 1)))
                .collect(),
        );

        pacific
            .intersection(&atlantic)
            .map(|x| vec![x.0, x.1])
            .collect()
    }

    fn bfs(
        heights: &Vec<Vec<i32>>,
        starts: Vec<(i32, i32)>,
    ) -> std::collections::HashSet<(i32, i32)> {
        let (max_r, max_c) = (heights.len(), heights[0].len());
        let mut queue = std::collections::VecDeque::<(i32, i32)>::with_capacity(max_r * max_c);
        let mut visited: std::collections::HashSet<(i32, i32)> = std::collections::HashSet::new();

        for (r, c) in starts {
            queue.push_back((r, c));
            visited.insert((r, c));
        }

        while !queue.is_empty() {
            let (r, c) = queue.pop_front().unwrap();

            for (dr, dc) in DIR.iter() {
                let (nr, nc) = (r + dr, c + dc);

                if nr >= 0 && nr < max_r as i32 && nc >= 0 && nc < max_c as i32 {
                    if !visited.contains(&(nr, nc))
                        && heights[nr as usize][nc as usize] >= heights[r as usize][c as usize]
                    {
                        queue.push_back((nr, nc));
                        visited.insert((nr, nc));
                    }
                }
            }
        }
        visited
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_417() {
        let mut result = Solution::pacific_atlantic(vec![
            vec![1, 2, 2, 3, 5],
            vec![3, 2, 3, 4, 4],
            vec![2, 4, 5, 3, 1],
            vec![6, 7, 1, 4, 5],
            vec![5, 1, 1, 2, 4],
        ]);
        result.sort_by_cached_key(|x| (x[0], x[1]));

        let mut expected = vec![
            vec![0, 4],
            vec![1, 3],
            vec![1, 4],
            vec![2, 2],
            vec![3, 0],
            vec![3, 1],
            vec![4, 0],
        ];

        expected.sort_by_cached_key(|x| (x[0], x[1]));

        assert_eq!(result, expected);
    }
}
