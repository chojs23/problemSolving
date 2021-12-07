def solution(new_id):
    answer = ''
    temp = new_id.lower()

    for x in temp:
        if x == "-" or x == "_" or x == "." or x.isalpha() or x.isdigit():
            answer += x

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == "." and len(answer) == 1:
        answer = ""
    elif answer[0] == ".":
        answer = answer[1:]
    elif answer[-1] == ".":
        answer = answer[:-1]

    if not answer:
        answer += "a"
    else:
        answer = answer[:15]

    if len(answer) > 15:
        answer = answer[:15]

        if answer[-1] == ".":
            answer = answer[:-1]
    if answer[-1] == ".":
        answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) != 3:
            answer += answer[-1]

    return answer
