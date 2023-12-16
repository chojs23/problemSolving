# SET
def solution(input_string):
    answer = set()
    last = ""
    seen = set()

    for input in input_string:
        if not last:
            last = input
            seen.add(input)
            continue
        if last == input:
            continue

        if input not in seen:
            last = input
            seen.add(input)
            continue
        else:
            answer.add(input)
            last = input
    if not answer:
        return "N"

    return "".join(sorted(answer))
