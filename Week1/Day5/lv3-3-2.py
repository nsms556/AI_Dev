def solution(dirs):
    answer = 7

    preset = {'U':(-1,0), 'L':(0,-1), 'D':(1,0), 'R':(0,1)}
    x = 5
    y = 5

    hori = set()
    vert = set()

    for d in list(dirs) :
        addY, addX = preset[d]

        if x+addX < 0 or x+addX > 10 or y+addY > 10 or y+addY < 0:
            continue
            
        x += addX
        y += addY
        
        if d == 'U' :
            vert.add((y, x))
        elif d == 'D' :
            vert.add((y-1, x))
        elif d == 'L' :
            hori.add((y, x))
        elif d == 'R' :
            hori.add((y, x-1))

    answer = len(hori) + len(vert)

    return answer