import sys
N = int(input())
sav = [0]
now = [0]
for n in range(N):
    sav.append(int(sys.stdin.readline()))
now.append(sav[1])
if N>1:
    now.append(sav[1]+sav[2])
    for n in range(3, N+1):
        now.append(max(now[n-1], now[n-2]+sav[n], now[n-3]+sav[n-1]+sav[n]))
print(now[-1])
