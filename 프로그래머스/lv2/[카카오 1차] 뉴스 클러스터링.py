def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = []
    set2 = []
    l, r = 0, 1
    while r < len(str1):
        if str1[l].isalpha() and str1[r].isalpha():
            set1.append(str1[l] + str1[r])
        l += 1
        r += 1
    l, r = 0, 1
    while r < len(str2):
        if str2[l].isalpha() and str2[r].isalpha():
            set2.append(str2[l] + str2[r])
        l += 1
        r += 1

    # s1_copy = set1.copy()
    s2_copy = set2.copy()

    # 교집합
    inter = []
    for i in set1:
        if i in s2_copy:
            inter.append(i)
            # s1_copy.remove(i)
            s2_copy.remove(i)

    child = len(inter)
    parent = len(set1) + len(set2) - child
    if parent <= 0:
        return 65536
    answer = int((child / parent) * 65536)
    return answer
