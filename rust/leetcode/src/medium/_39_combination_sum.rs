//Backtracking

struct Solution;

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];
        let mut path = vec![];

        Self::dfs(0, &mut path, &candidates, target, &mut result);

        result
    }

    fn dfs(
        start: usize,
        path: &mut Vec<i32>,
        candidates: &Vec<i32>,
        target: i32,
        result: &mut Vec<Vec<i32>>,
    ) {
        if path.iter().sum::<i32>() == target {
            result.push(path.to_vec());
            return;
        }

        if path.iter().sum::<i32>() > target {
            return;
        }

        for i in start..candidates.len() {
            path.push(candidates[i]);
            Self::dfs(i, path, candidates, target, result);
            path.pop();
        }
    }
}

#[test]
fn test() {
    assert_eq!(
        Solution::combination_sum(vec![2, 3, 6, 7], 7),
        vec![vec![2, 2, 3], vec![7]]
    );
    assert_eq!(
        Solution::combination_sum(vec![2, 3, 5], 8),
        vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]]
    );
}
