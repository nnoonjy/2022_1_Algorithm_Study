import sys
M, N = map(int, input().split())
sav = [[-1]*(M+2)]+[]
now = []
newnow = []
cnt = 0
for n in range(N):
    sav.append([-1]+list(map(int, sys.stdin.readline().split()))+[-1])
    for m in range(M+2):
        if sav[n+1][m] == 1:
            now.append([n+1,m])
sav += [[-1]*(M+2)]
while True:
    for l in now:
        a = l[0]
        b = l[1]
        if sav[a-1][b] == 0:
            newnow.append([a-1,b])
            sav[a-1][b] = 1
        if sav[a+1][b] == 0:
            newnow.append([a+1,b])
            sav[a+1][b] = 1
        if sav[a][b-1] == 0:
            newnow.append([a,b-1])
            sav[a][b-1] = 1
        if sav[a][b+1] == 0:
            newnow.append([a,b+1])
            sav[a][b+1] = 1
    now = newnow
    newnow = []
    if now == []:
        break
    else:
        cnt += 1
p = 0
for n in range(1,N):
    if 0 in sav[n]:
        p = 1
        print(-1)
        break
if p == 0:
    print(cnt)
