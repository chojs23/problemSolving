from itertools import combinations


def solution(relation):
    # key의 개수
    N = len(relation[0])
    key_idx = list(range(N))
    candidate_keys = []
    for i in range(1, N + 1):
        for comb in combinations(key_idx, i):
            hist = []
            for rel in relation:
                current_key = [rel[c] for c in comb]
                print(current_key)
                # 하나라도 중복되는 경우: 식별 불가능
                if current_key in hist:
                    break
                else:
                    hist.append(current_key)
            # 하나도 중복 안 된 경우: 식별 가능
            else:
                for ck in candidate_keys:
                    # 최소성 확인
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidate_keys.append(comb)

    return len(candidate_keys)
