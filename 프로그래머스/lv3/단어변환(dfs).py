from collections import deque

# queue를 위함


def check(s, begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, []])

    while queue:
        n, l = queue.popleft()
        for word in words:
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                temp = l[0:]
                print(temp)
                temp.append(word)
                queue.append([word, temp])

    return 0


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
