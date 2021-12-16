def solution(n, lost, reserve):
    reserve.sort(reverse=True)
    for i in reserve:
        if i - 1 == lost[-1] or i + 1 == lost[-1]:
            lost.pop()

        if len(lost) == 0:
            break
    answer = 0
    srt = {}
    srt.setdefault()
    print(srt)
    s = []
    s.sort()
    sorted()


print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))
