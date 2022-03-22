def solution(files):
    answer = []
    head = []
    number = []
    tail = []

    for file in files:
        i = 0
        h = ""
        n = ""
        t = ""
        while i < len(file):
            if not file[i].isnumeric() and n == "":
                h += file[i]
            elif file[i].isnumeric() and t == "":
                n += file[i]
            else:
                t += file[i]
            i += 1

        head.append(h)
        number.append(n)
        tail.append(t)

    # print(head,number,tail)
    temp = []
    for i in range(len(files)):
        temp.append([head[i], number[i], tail[i]])
    # print(temp)
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    for i in range(len(files)):
        answer.append("".join(temp[i]))
    return answer
