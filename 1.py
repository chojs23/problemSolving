def solution(new_id):
    answer = ''
    temp = new_id.lower()

    for x in temp:
        if x == "-" or x == "_" or x == "." or x.isalpha() or x.isdigit():
            answer += x

    for i, c in enumerate(answer):
        print(i, c)
        if i < len(answer):
            while answer[i] == "." and answer[i+1] == ".":
                answer = answer[:i]+answer[i+1:]
    answer.find
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
        answer = answer[:16]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) < 3:
        while len(answer) > 2:
            answer += answer[-1]

    return answer


print(solution(	"=.="))
