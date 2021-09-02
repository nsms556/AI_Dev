# 0901 광고삽입
# https://programmers.co.kr/learn/courses/30/lessons/72414


def time_to_int(t) :
    h, m, s = map(int, t.split(':'))
    
    return h * 3600 + m * 60 + s

def int_to_time(i) :
    h = i // 3600
    m = (i % 3600) // 60
    s = i % 60

    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

def solution(play_time, adv_time, logs) :
    answer = ''
    
    pt = time_to_int(play_time)
    at = time_to_int(adv_time)
    viewer = [0 for k in range(pt+1)]

    for log in logs :
        start, end = map(time_to_int, log.split('-'))

        viewer[start] += 1
        viewer[end] -= 1

    for i in range(1, pt+1) :
        viewer[i] += viewer[i-1]

    for i in range(1, pt+1) :
        viewer[i] += viewer[i-1]

    #print(viewer)

    max_view, max_time = 0, 0

    for i in range(at - 1, pt) :
        if i >= at :
            #print(i, viewer[i] - viewer[i - at], end='   ')
            ##if i % 10 == 0 :
                #print()
            if max_view < viewer[i] - viewer[i - at] :
                max_view = viewer[i] - viewer[i - at]
                max_time = i - at + 1
        else :
            if max_view < viewer[i] :
                max_view = viewer[i]
                max_time = i - at + 1

    answer = int_to_time(max_time)

    return answer

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))
