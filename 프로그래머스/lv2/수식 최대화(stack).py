from itertools import permutations


def solution(expression):
    answer = 0
    n = len(expression)
    operators = ["*", "+", "-"]

    def make_exp():
        temp = ""
        exp = []
        for i in expression:
            if i.isnumeric():
                temp += i
            else:
                exp.append(int(temp))
                exp.append(i)
                temp = ""
        exp.append(int(temp))
        return exp

    for i in permutations(operators, 3):
        exp = make_exp()
        for op in i:
            while op in exp:
                idx = exp.index(op)
                if op == "+":
                    cal = exp[idx - 1] + exp[idx + 1]
                if op == "-":
                    cal = exp[idx - 1] - exp[idx + 1]
                if op == "*":
                    cal = exp[idx - 1] * exp[idx + 1]
                exp = exp[: idx - 1] + [cal] + exp[idx + 2 :]
        answer = max(answer, abs(exp[0]))
    return answer
