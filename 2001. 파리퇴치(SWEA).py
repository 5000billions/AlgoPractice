T = int(input())
for tc in range( 1 , T + 1 ):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    many_kill = 0

    for r in range( N - M + 1 ):
        for c in range( N - M + 1):
            kill = 0
            for i in range( M ):
                for j in range( M ):
                    kill += grid[ r + i ][ c + j ]

            many_kill = max( many_kill, kill )

    print(f'#{tc} {many_kill}')
