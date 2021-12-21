def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    i = 1
    while True:
        if len(arr) < 2:
            answer = arr

            break
        if arr[i - 1] == arr[i]:
            i += 1
        else:
            answer.append(arr[i - 1])
            i += 1
        if i == len(arr):
            answer.append(arr[i - 1])
            break

    return answer
