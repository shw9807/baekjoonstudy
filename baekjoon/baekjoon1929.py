M,N = map(int,input().split())
if M == 1:
    M = 2
n = list(range(M, N+1))
for i in range(M, N+1):
    for j in range(2,int((i**0.5)+1)):
        if i%j == 0:
            n.remove(i)
            break
for i in sorted(n):
    print(i)