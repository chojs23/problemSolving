def solution(msg):
    answer = []
    sheet = {}
    for i, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        sheet[s] = i + 1

    i = 0
    while i < len(msg):
        cnt = 1
        tmp = ""
        tmp += msg[i]

        while i + 1 < len(msg) and tmp + msg[i + 1] in sheet:
            tmp += msg[i + 1]
            cnt += 1
            i += 1

        if i + 1 < len(msg):
            sheet[tmp + msg[i + 1]] = len(sheet) + 1

        answer.append(sheet[tmp])
        i += 1

    return answer
