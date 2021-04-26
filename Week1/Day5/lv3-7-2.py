def solution(n):
    vt = [False] * n
    ru = [False] * (2 * n - 1)
    rd = [False] * (2 * n - 1)
    count = 0
    
    def dfs(n, row) :
        nonlocal count

        if row == n :
            count += 1
            return

        for col in range(n) :
            ruidx = row + col
            rdidx = row - col + n - 1

            if not (vt[col] or ru[ruidx] or rd[rdidx]) :
                vt[col] = ru[ruidx] = rd[rdidx] = True
                dfs(n, row+1)
                vt[col] = ru[ruidx] = rd[rdidx] = False

    dfs(n, 0)

    return count