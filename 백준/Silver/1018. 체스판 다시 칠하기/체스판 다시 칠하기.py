n, m = map(int, input().split())
board = [input() for _ in range(n)]  # m이 아닌 n으로 수정

result = []

for i in range(n - 7):  # 보드의 크기를 기준으로 수정
    for j in range(m - 7):  # 보드의 크기를 기준으로 수정
        black = 0
        white = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        white += 1
                    if board[a][b] != 'B':
                        black += 1
                else:
                    if board[a][b] != 'B':
                        white += 1
                    if board[a][b] != 'W':
                        black += 1

        result.append(black)
        result.append(white)

print(min(result))
