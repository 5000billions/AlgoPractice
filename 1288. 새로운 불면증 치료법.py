T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = []
    lamb = 0
    
    while len(arr) < 10:
        lamb += N
        idx = list(str(lamb))

        for i in idx:
            if i not in arr:
                arr.append(i)

    print(f"#{tc} {lamb}")