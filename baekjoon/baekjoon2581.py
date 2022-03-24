import sys
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
result = []
for i in range(x, y+1):
    divisor = 0
    for n in range(2, i):
        if i%n == 0:
            divisor += 1
    if divisor == 0:
        if i != 1:
            result.append(i)
if len(result) != 0:
    print(sum(result))
    print(min(result))
if len(result) == 0:
    print(-1)