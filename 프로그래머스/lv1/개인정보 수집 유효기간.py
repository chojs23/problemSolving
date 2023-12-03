def parseDate(date: str):
    # "2022.05.19"
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    return year, month, day


def addMonth(date: str, add: int) -> str:
    year, month, day = parseDate(date)
    month += add

    # add value can up to 100
    while month > 12:
        year += 1
        month -= 12

    # month and day will be 2 digits
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)

    return str(year) + "." + str(month) + "." + str(day)


def compareDate(today: str, date: str) -> bool:
    todayYear, todayMonth, todayDay = parseDate(today)
    year, month, day = parseDate(date)

    if todayYear > year:
        return True
    elif todayYear == year:
        if todayMonth > month:
            return True
        elif todayMonth == month:
            if todayDay >= day:
                return True

    return False


def solution(today: str, terms: list[str], privacies: list[str]) -> list[str]:
    answer = []

    termsDict = {}
    for i in range(len(terms)):
        name, expiration = terms[i].split(" ")
        termsDict[name] = expiration

    print(termsDict)

    for idx, privacy in enumerate(privacies):
        date, term = privacy.split(" ")
        print(date, term)
        if compareDate(today, addMonth(date, int(termsDict[term]))):
            answer.append(idx + 1)

    print(answer)
    return answer


solution("2020.02.10", ["A 1", "B 100"], ["2019.02.10 A", "2019.02.10 B"])
