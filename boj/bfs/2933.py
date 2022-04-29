from sys import stdin

input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 미네랄 떨어질 수 있는지 칸 세기
def checkDownCnt(fallLst, check):
    downCnt, flag = 1, 0  # downCnt 크기 1씩 늘려가며
    while True:
        for r, c in fallLst:
            if r + downCnt == R - 1:  # 땅을 만나거나
                flag = 1
                break
            if (
                cave[r + downCnt + 1][c] == "x" and check[r + downCnt + 1][c]
            ):  # 다른 미네랄 만나면
                flag = 1
                break
        if flag:  # 그 때가 떨어질 수 있는 최대 downCnt 값
            break
        downCnt += 1
    return downCnt


def checkLand():
    check = [[0] * C for _ in range(R)]
    # 땅에 붙어 있는 미네랄 check 배열에 표시
    for lc in range(C):
        if cave[R - 1][lc] == "x" and not check[R - 1][lc]:  # 미네랄이면서 첫 방문이면
            check[R - 1][lc] = 1
            Q = deque([(R - 1, lc)])
            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):  # 격자 밖이면
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:  # 미네랄이거나 방문한 적 없으면
                        check[nr][nc] = 1
                        Q.append((nr, nc))
    return check


def breakMinerals(br, bc):
    # 2단계 - 땅에 붙어 있는 미네랄 1로 표시되어 있는 맵 리턴
    check = checkLand()

    # 3단계 - 공중에 떠있는 미네랄 2로 표시, 동굴에서 지우기
    minerals = []  # 공중에 떠있는 미네랄 리스트
    fallLst = []  # 떨어질 수 있는 클러스터의 아랫부분만 저장
    for nd in range(4):  # 깨진 곳 기준으로 4방향 확인
        r = br + dr[nd]
        c = bc + dc[nd]
        if not (0 <= r < R and 0 <= c < C):
            continue

        # 미네랄인데 땅에 붙어 있지 않다면(check 배열에서 0으로 표시되어 있다면) 2로 표시
        if cave[r][c] == "x" and not check[r][c]:
            Q = deque([(r, c)])
            check[r][c] = 2
            minerals.append((r, c))
            cave[r][c] = "."
            while Q:
                r, c = Q.popleft()
                if cave[r + 1][c] == ".":  # 바로 밑이 빈 공간인 미네랄
                    fallLst.append((r, c))
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 2  # 공중에 떠있는 미네랄 클러스터 표시
                        Q.append((nr, nc))
                        minerals.append((nr, nc))  # 미네랄 위치 리스트에 담기
                        cave[nr][nc] = "."  # 동굴에서 공중에 떠 있는 미네랄 제거

    if fallLst:  # 공중에 떠있는 미네랄이 있다면
        # 4단계 - 떨어질 최대 칸의 수 리턴
        downCnt = checkDownCnt(fallLst, check)

        # 5단계 - 미네랄 떨어질 위치 동굴에 그리기
        for mr, mc in minerals:
            cave[mr + downCnt][mc] = "x"


# main
R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

# 1단계 - 좌우에서 막대기 던져 미네랄 깨기
for i in range(N):
    br = R - heights[i]
    if not i % 2:  # 왼쪽에서 깸
        for bc in range(C):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)  # 깨진 위치 인자로 넘겨 미네랄 깨기
                break
    else:  # 오른쪽에서 깸
        for bc in range(C - 1, -1, -1):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)
                break

# 형식에 맞게 출력
for row in cave:
    print("".join(row))
