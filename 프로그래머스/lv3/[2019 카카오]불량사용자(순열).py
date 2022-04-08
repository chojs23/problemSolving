from itertools import permutations


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False  # 현재 튜플 불일치

    return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    banned_Set = []

    for users in user_permutation:
        # 하나의 튜플과 비교 시작
        if not check(users, banned_id):
            continue  # 다음 튜플 가져오기
        else:
            # print(users)
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)

    return len(banned_Set)
