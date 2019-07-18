def check(sett):
    for i in range(0,10):
        if not i in sett:
            return True
    return False

for rounds in range(int(input())):
    N = int(input())
    num = N
    gop = 1
    sett = set()
    
    while check(sett):
        a = set(map(int,list(str(N * gop))))
        gop += 1
        sett = sett | a

    print(f'#{rounds + 1} {(gop-1) * (N)}')
