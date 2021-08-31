# 0825 직업군 추천하기
# https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    newTable = []
    for item in table :
        newTable.append(item.split())
        
    scores = []
    for cat in newTable :
        catScore = 0
        for i in range(len(languages)) :
            if languages[i] in cat :
                catScore += preference[i] * (6 - cat.index(languages[i]))
        scores.append(catScore)
    answer = [newTable[i][0] for i, val in enumerate(scores) if val == max(scores)]
    
    return sorted(answer)[0]