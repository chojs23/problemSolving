def solution(board, moves):
    box = []
    answer = 0

    for i in moves:
        i = i - 1

        for j in range(len(board)):
            if board[j][i] == 0:
                continue
            else:
                box.append(board[j][i])
                if len(box) > 1 and box[-1] == box[-2]:
                    box.pop()
                    box.pop()
                    answer += 2
                board[j][i] = 0
                break

    return answer
