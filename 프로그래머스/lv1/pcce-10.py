# Implementation
def solution(data, ext, val_ext, sort_by):
    answer = [[]]

    data_dict = {}
    data_dict["code"] = 0
    data_dict["date"] = 1
    data_dict["maximum"] = 2
    data_dict["remain"] = 3

    sort_by = data_dict[sort_by]

    answer = extract(data, ext, val_ext)
    answer = sorted(answer, key=lambda x: x[sort_by])
    return answer


def extract(data, ext, val_ext):
    data_dict = {}
    data_dict["code"] = 0
    data_dict["date"] = 1
    data_dict["maximum"] = 2
    data_dict["remain"] = 3

    target_idx = data_dict[ext]

    result = []
    for d in data:
        if d[target_idx] < val_ext:
            result.append(d)

    return result


# test code
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]

print(solution(data, "date", 20300501, "remain"))
