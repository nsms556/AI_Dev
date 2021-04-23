'''def solution(numbers):
    answer = []
    fours = []
    
    for num in numbers :
        tmp = ''
        while len(tmp) < 4 :
            tmp += str(num)
        if len(tmp) > 4 :
            tmp = tmp[:4]
        fours.append(int(tmp))
        
    for _ in range(len(fours)) :
        idx = fours.index(max(fours))
        answer.append(str(numbers[idx]))
        numbers.remove(numbers[idx])
        fours.remove(fours[idx])

    return ''.join(answer)'''

def solution(numbers):
    nums = sorted(numbers, key=lambda x : (str(x) * 4)[:4], reverse=True)
    nums = list(map(str, nums))
    
    if nums[0] == '0' :
        answer = '0'
    else :
        answer = ''.join(nums)
        
    return answer

print(solution([2,1,0]))