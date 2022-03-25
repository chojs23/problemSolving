def solution(infos, queries):
    answer = []
    info_dict = {}

    for lang in ["cpp", "java", "python", "-"]:
        for job in ["backend", "frontend", "-"]:
            for career in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    info_dict[lang + job + career + food] = []

    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        info_dict[lang + job + career + food].append(int(info[4]))
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.replace(" and ", "")
        query = query.split()
        query_score = int(query[1])
        query = query[0]

        length = len(info_dict[query])
        l, r = 0, length - 1
        tmp = r + 1
        while l <= r:
            mid = (l + r) // 2

            if query_score > info_dict[query][mid]:
                l = mid + 1
            else:
                r = mid - 1
        answer.append(tmp - l)

    return answer
