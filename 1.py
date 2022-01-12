def solution(name):
    answer = 0
    length = len(name)
    alphabet = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    cursor = 0
    for i in range(length):
        if name[i] == "A":
            pass
        else:
            # move cursor

            answer += min(i - cursor, (length - i + cursor))
            cursor = i
            # Change alphabet
            alpha_idx = alphabet.index(name[i])
            answer += min(alpha_idx, len(alphabet) - alpha_idx)

    return answer


print(solution("ZAAAZZZZZZZ"))  # 15
