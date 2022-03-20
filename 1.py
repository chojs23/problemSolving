def solution(s):
    answer = ""

    s = s.lower()

    words = s.split(" ")

    for word in words:
        if word == " ":
            continue
        if word[0].isalpha():
            answer += word[0].upper() + word[1:]
        else:
            answer += word
        answer += " "

    return answer[:-1]


s = []
solution("Hi   my  name")
