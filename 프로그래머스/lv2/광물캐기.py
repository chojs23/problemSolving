from itertools import permutations


def mining(pick, mineral):
    if pick == 0:
        return 1
    elif pick == 1:
        if mineral == "diamond":
            return 5
        return 1
    else:
        if mineral == "diamond":
            return 25
        if mineral == "iron":
            return 5
        return 1


def solution2(picks, minerals):
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[: sum(picks) * 5]
    answer = 0
    length = len(minerals) // 5
    mod = len(minerals) % 5
    if mod != 0:
        length += 1
    print(length)

    arr = []

    for i in range(length):
        mineral = minerals[i * 5 : (i + 1) * 5]
        stone, iron, diamond = 0, 0, 0
        for j in range(len(mineral)):
            stone += mining(2, mineral[j])
            iron += mining(1, mineral[j])
            diamond += mining(0, mineral[j])
        arr.append([stone, iron, diamond])

    print(arr)

    arr = sorted(arr, key=lambda x: -x[0])

    cursor = 0

    for i, p in enumerate(picks):
        for _ in range(p):
            if i == 0:
                answer += arr[cursor][2]
            elif i == 1:
                answer += arr[cursor][1]
            else:
                answer += arr[cursor][0]
            cursor += 1
            if cursor == length:
                break
        if cursor == length:
            break

    return answer


def solution(picks, minerals):
    answer = 25 * 50

    pick_list = []

    for i, pick in enumerate(picks):
        for _ in range(pick):
            pick_list.append(i)

    perm = set(permutations(pick_list))

    for p in perm:
        cursor = 0
        total = 0
        for i in p:
            for _ in range(5):
                total += mining(i, minerals[cursor])
                cursor += 1
                if cursor == len(minerals):
                    break
            if cursor == len(minerals):
                break
        print(total)
        answer = min(answer, total)

    return answer
