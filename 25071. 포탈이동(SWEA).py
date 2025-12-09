T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [0] + list(map(int, input().split()))

    now = 1
    cnt = 0

    while now < N:
        if P[now] != 0 :
            temp = P[now]
            P[now] = 0
            now = temp
        else:
            now += 1
        cnt += 1

    print(f'#{tc} {cnt}')