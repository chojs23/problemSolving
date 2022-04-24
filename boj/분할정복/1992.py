import sys

input = sys.stdin.readline

N = int(input())

image = [list(map(int, input().rstrip())) for _ in range(N)]


def quadtree(x, y, n):
    # n = 1, 하나의 픽셀만 볼 경우,
    if n == 1:
        return str(image[x][y])

    result = []
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색이 다르면, 다시 분할하자.
            if image[i][j] != image[x][y]:
                result.append("(")
                result.extend(quadtree(x, y, n // 2))
                result.extend(quadtree(x, y + n // 2, n // 2))
                result.extend(quadtree(x + n // 2, y, n // 2))
                result.extend(quadtree(x + n // 2, y + n // 2, n // 2))
                result.append(")")
                return result

    return str(image[x][y])


print("".join(quadtree(0, 0, N)))
