import re


def solution(word, pages):
    total_score = []
    basic_score = {}
    exlink_cnt = {}
    to_me_link = {}

    for page in pages:
        title = re.search(
            '<meta property="og:url" content="(https://\S+)"', page
        ).group(1)
        print(title)
        basic_score[title] = 0
        exlink_cnt[title] = 0

        for find in re.findall("[a-zA-Z]+", page):
            if find.upper() == word.upper():
                basic_score[title] += 1

        for link in re.findall('<a href="(https://\S+)"', page):
            exlink_cnt[title] += 1
            if link in to_me_link:
                to_me_link[link].append(title)
            else:
                to_me_link[link] = [title]

    for curr in basic_score:
        link_score = 0
        if curr in to_me_link:
            for ex in to_me_link[curr]:
                link_score += basic_score[ex] / exlink_cnt[ex]
        total_score.append(basic_score[curr] + link_score)

    return total_score.index(max(total_score))
