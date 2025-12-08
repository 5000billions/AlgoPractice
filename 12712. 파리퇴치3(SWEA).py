T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    plus = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    x = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

    max_sum = 0

    for i in range(N):
        for j in range(N):
            center = grid[i][j]

            plus_sum = center
            for di, dj in plus:
                for d in range(1, M):
                    r, c = i + di * d, j + dj * d
                    if 0 <= r < N and 0 <= c < N:
                        plus_sum += grid[r][c]
                    else:
                        break 

            x_sum = center
            for di, dj in x:
                for d in range(1, M):
                    r, c = i + di * d, j + dj * d
                    if 0 <= r < N and 0 <= c < N:
                        x_sum += grid[r][c]
                    else:
                        break

            max_sum = max(x_sum, plus_sum, max_sum)

    print(f'#{tc} {max_sum}')