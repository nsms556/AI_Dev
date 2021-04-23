'''
풀이 영상에 포함되지 않는 테스트 케이스
1개로 표현 가능한 경우(N == number)
'''

def solution(N, number):
    answer = -1
    
    make = [set() for _ in range(8)]

    for idx, x in enumerate(make, start=1) :
        x.add(int(str(N) * idx))

    for i in range(len(make)) :
        for j in range(i) :
            for oper1 in make[j] :
                for oper2 in make[i-j-1] :
                    make[i].add(oper1 + oper2)
                    make[i].add(oper1 - oper2)
                    make[i].add(oper1 * oper2)
                    if oper2 != 0 :
                        make[i].add(oper1 // oper2)

        if number in make[i] :
            answer = i + 1
            break
    
    return answer

print(solution(5, 12))
print(solution(2, 11))
print(solution(2, 2))