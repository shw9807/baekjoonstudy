import math
a,b=map(int,input().split())
count = 0
for i in range(a, b+1):
    for n in range(2, int(math.sqrt(b+1))):
        d = 0
        c = n*n
        if i%c == 0 :
            d += 1
    if d == 0:
        count += 1
print(count)