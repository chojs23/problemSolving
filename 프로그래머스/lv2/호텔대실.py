def solution(book_time):
    answer = 0

    book_time = [list(map(time_to_int, time)) for time in book_time]

    sorted_book_time = sorted(book_time, key=lambda x: x[0])

    room = {1: (sorted_book_time[0][0], sorted_book_time[0][1])}

    for i in range(1, len(sorted_book_time)):
        start, end = sorted_book_time[i]
        for key in room.keys():
            if room[key][1] + 10 <= start:
                room[key] = (start, end)
                break
        else:
            room[len(room) + 1] = (start, end)

    answer = len(room)

    return answer


def time_to_int(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
