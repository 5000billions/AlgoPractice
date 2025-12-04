T = int(input())
for tc in range( 1 , T + 1 ):
    '''
    P = A사 리터당 돈
    Q = B사 기본 요금
    R = 리터 이하일시 Q 요금
    S = 리터 초과시 Q 요금
    W = 총 사용량
    '''
    
    P, Q, R, S, W = map(int, input().split())
print(P)

      