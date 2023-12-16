# DFS
def query(gen, index):
    if gen == 1:
        return "Rr"
    parent_gene = query(gen - 1, index // 4)

    if parent_gene == "RR":  # 유전자가 같은 경우.
        return "RR"
    if parent_gene == "rr":
        return "rr"

    # 유전자가 갈라지는 경우
    local_index = index % 4

    if local_index == 0:
        return "RR"
    if local_index in (1, 2):
        return "Rr"
    return "rr"


def solution(queries):
    answer = []

    for gen, index in queries:
        answer.append(query(gen, index - 1))

    return answer
