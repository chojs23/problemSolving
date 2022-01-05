def make_dp(dp, n):
    if dp[n] == "0":
        qoutient, remainder = divmod(n, 3)
        if remainder != 0:
            if dp[qoutient] == "0":
                make_dp(dp, qoutient)
            dp[n] = dp[qoutient] + dp[remainder]
        else:
            if dp[qoutient - 1] == "0":
                make_dp(dp, qoutient - 1)
            dp[n] = dp[qoutient - 1] + "4"
    else:
        return dp[n]


def solution(n):
    answer = ""
    if n < 3:
        return "1" if n == 1 else "2"
    dp = ["0"] * (n + 1)
    # 1 2 4 11 12 14 21 22 24 41 42 44(12,4,0) 111(13,4,1) 112(14,4,2) 114(15,5,0) 121 122 124  224(27,9,0) 241(28,9,1)
    dp[1] = "1"
    dp[2] = "2"
    dp[3] = "4"

    make_dp(dp, n)
    print(dp)

    return dp[-1]


solution(14)
