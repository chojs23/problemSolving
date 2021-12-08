def solution(s):
    answer = 0
    word = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # w={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    w = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    digit = 0
    temp = s
    for x in w:
        if x in s:
            temp = temp.replace(x, w[x])

    answer = int(temp)
    return answer
