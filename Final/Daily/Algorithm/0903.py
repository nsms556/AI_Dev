def solution(word):
    answer = 0
    d = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    s = [781, 156, 31, 6, 1]

    for i, c in enumerate(word) :
        answer += (s[i] * d[c] + 1)

    return answer

word = "AAAAE"
print(solution(word))

word = "AAAE"
print(solution(word))

word = "I"
print(solution(word))

word = "EIO"
print(solution(word))

'''
a____   1
e____   782
i____   1563
o____   2344
u____   3125

aa___   2
ae___   158
ai___   314
ao___   470
au___   626

aaa__   3
aae__   34
aai__   65
aao__   96
aau__   127

aaaa_   4
aaae_   10
aaai_   16
aaao_   22
aaau_   28

aaaaa   5   
aaaae   6
aaaai   7
aaaao   8
aaaau   9
'''