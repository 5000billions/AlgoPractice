T = int(input())
for tc in range( 1 , T + 1 ):
    '''
    P = A사 리터당 돈
    Q = B사 기본 요금
    R = R리터 이하일시 Q 기본요금
    S = R리터 초과시 리터당 추가 요금
    W = 총 사용량
    '''
    
    P, Q, R, S, W = map(int, input().split())

    A_use = P * W
    B_use = 0

    if R < W:
        B_use = Q + (W - R) * S
    else: 
        B_use = Q

    Cheap_Company = min(A_use, B_use)

    print(f'#{tc} {Cheap_Company}')