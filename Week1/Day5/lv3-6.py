def solution(board, nums):
    n = len(board)
    bingo = {}

    hori = [0] * n
    vert = [0] * n
    diag = [0] * 2

    for i in range(n) :
        for j in range(n) :
            bingo[board[i][j]] = (i, j)

    for num in nums :
        y, x = bingo[num]

        hori[x] += 1
        vert[y] += 1

        if x == y :
            diag[0] += 1
        if y == n - x - 1 :
            diag[1] += 1

    print(hori, vert, diag)
    return (hori.count(n) + vert.count(n) + diag.count(n))

print(solution([[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]], [14,3,2,4,13,1,16,11,5,15]))
print(solution([[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]], [15,7,2,25,9,16,12,18,5,4,10,13,20]))
print(solution([[1,2,3], [4,5,6], [7,8,9]], [1,5,9,7,3]))