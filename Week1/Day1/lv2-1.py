def solution(brown, red):
    answer = []

    redHeights = [i for i in range(1, int(red ** 0.5)+1) if red % i == 0]

    for rHeight in redHeights :
        rWidth = red // rHeight
        
        bNeeds = ((rHeight+2) + (rWidth+2)) * 2 - 4
        if bNeeds == brown :
            answer = [rWidth+2, rHeight+2]
            break

    return answer

b = 24
r = 24

print(solution(b, r))