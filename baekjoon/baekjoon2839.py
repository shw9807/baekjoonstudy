n = int(input())
result = []
for i in range(0, int(n/3)+1):
    for j in range(0,int(n/5)+1):
        if 3*i + 5*j == n :
            result.append(i+j)
if len(result) == 0:
    print(-1)
else:
    print(min(result))