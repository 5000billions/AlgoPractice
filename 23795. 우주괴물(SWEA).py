T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    jail = [list(map(int, input().split())) for _ in range(N)]

    monitoring = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    vision = 0
    total_path = 0

    for i in range(N):
        for j in range(N):
            security = jail[i][j]

            if security == 0:
                total_path += 1

            if security == 2:
                
                for di, dj in monitoring:

                    for d in range( 1, N ):
                        r, c = i + di * d, j + dj * d
                        if not (0 <= r < N and 0 <= c < N):
                            break

                        if jail[r][c] == 1:
                            break

                        if jail[r][c] == 0:
                            vision += 1

    ans = total_path - vision

    print(f'#{tc} {ans}')