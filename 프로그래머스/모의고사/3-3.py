

def solution(distance, scope, times):
    guards = []

    for _scope, _times in zip(scope, times):
        start, end = min(_scope), max(_scope)
        guards.append([start, end, _times[0], _times[1]])
    guards.sort(key=lambda x: x[0])

    print(f"guards: {guards}")

    for start, end, work, rest in guards:
        cycle = (work+rest)
        cnt_cycle = (start-1)//cycle
        start -= cnt_cycle*cycle
        end -= cnt_cycle*cycle

        print(f"start: {start},end: {end}")
        if start <= work:
            return cnt_cycle*cycle+start
        if end > cycle:
            return cnt_cycle*cycle+cycle+1

    return distance
