from collections import deque


def solution(record):
    answer = []
    q = deque()
    name = {}
    for rec in record:
        tmp = rec.split()
        if tmp[0] == "Enter":
            # 0 = Enter
            if tmp[1] not in name:
                name[tmp[1]] = tmp[2]
            else:
                name[tmp[1]] = tmp[2]
            q.append((0, tmp[1]))
        elif tmp[0] == "Leave":
            # 1 = Leave
            q.append((1, tmp[1]))
        else:
            name[tmp[1]] = tmp[2]
    while q:
        oper, id = q.popleft()
        if oper == 0:
            answer.append(("{}님이 들어왔습니다.".format(name[id])))
        elif oper == 1:
            answer.append(("{}님이 나갔습니다.".format(name[id])))

    return answer
