# permutaions, backtracking,dfs,brute force
from itertools import permutations


def solution(ability):
    answer = 0
    n_student = len(ability)
    n_ability = len(ability[0])

    comb = list(permutations(range(n_student), n_ability))

    for c in comb:
        _sum = 0
        for i in range(n_ability):
            _sum += ability[c[i]][i]
        answer = max(answer, _sum)

    return answer


maximum = 0


def dfs(ability, student, n_ability, visited, total, depth):
    global maximum
    total += ability[student][depth]
    if depth == n_ability - 1:
        maximum = max(maximum, total)
        return

    for i in range(len(ability)):
        if not visited[i]:
            visited[i] = 1
            temp = dfs(ability, i, n_ability, visited, total, depth + 1)
            visited[i] = 0

    return maximum


def sol2(ability):
    global maximum
    n_student = len(ability)
    n_ability = len(ability[0])

    for i in range(n_student):
        visited = [0] * n_student
        visited[i] = 1
        dfs(ability, i, n_ability, visited, 0, 0)
    print(maximum)

    return maximum


sol2([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
