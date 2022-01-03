def balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i
    return 0


def check_proper(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def reverse(p):
    temp = list(p)
    for i in range(len(temp)):
        if temp[i] == "(":
            temp[i] = ")"
        else:
            temp[i] = "("
    return "".join(temp)


def solution(p):

    if len(p) == 0:
        return ""
    u = p[: balanced_index(p) + 1]
    v = p[balanced_index(p) + 1 :]

    if check_proper(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u)[1:-1]
