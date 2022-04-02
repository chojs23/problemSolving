def solution(s):
    countT, window = {}, {}
    for c in s:
        countT[c] = 1
    have, need = 0, len(countT)
    res = [-1, -1]
    resLen = float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            if (r - l + 1) < resLen:
                res = [l + 1, r + 1]
                resLen = r - l + 1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1

    return res
