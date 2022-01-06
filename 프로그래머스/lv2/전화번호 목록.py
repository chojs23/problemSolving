def solution(phone_book):
    answer = True
    hashmap = {}
    for number in phone_book:
        hashmap[number] = 1
    for number in phone_book:
        jubdoo = ""
        for num in number:
            jubdoo += num
            if jubdoo in hashmap and jubdoo != number:
                answer = False
    return answer
