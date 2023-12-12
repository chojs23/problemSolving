def solution(numbers):
    answer = []
    for number in numbers:
        bits = list("0" + bin(number)[2:])
        idx = "".join(bits).rfind("0")
        bits[idx] = "1"
        if number % 2 == 1:
            bits[idx + 1] = "0"

        answer.append(int("".join(bits), 2))
    return answer
