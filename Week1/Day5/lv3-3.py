def solution(dirs):
    answer = 7

    preset = {'U':(-1,0), 'L':(0,-1), 'D':(1,0), 'R':(0,1)}
    x = 0
    y = 0

    visit = set()

    for d in list(dirs) :
        addY, addX = preset[d]

        dx, dy = x+addX, y+addY

        if dx > 5 or dx < -5 or dy > 5 or dy < -5 :
            continue

        if (x,y,dx,dy) not in visit :
            visit.add((x,y,dx,dy))
            visit.add((dx,dy,x,y))

        x, y = dx, dy

    answer = len(visit) // 2

    return answer

print(solution("ULURRDLLU"))
print(solution("ULURRDLLU"))
print(solution('LLLLLLLLL'))
print(solution('DDDDDDDDD'))
print(solution('RRRRRRRRR'))
print(solution('UUUUUUUUU'))
print(solution('UUUUURRRRRDDDDDDDDDDLLLLLLLLLLUUUUUUUUUURRRRRDDDDD'))
print(solution('UDUDUDUDLRLRLRLRDUDUDUDURLRLRL'))

'''
ULURRDLLU
5, 5
U 4, 5 -> vert 4,5
L 4, 4 -> hori 4,4
U 3, 4 -> vert 3,4
R 3, 5 -> hori 3,4
R 3, 6 -> hori 3,5
D 4, 6 -> vert 3,6
L 4, 5 -> hori 4,5
L 4, 4 -> hori 4,4
U 3, 4 -> vert 3,4
'''