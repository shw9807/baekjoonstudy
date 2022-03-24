N = int(input())
count = 0
num = list(map(int, input().split()))
for i in range(N) :
    measure = []
    if num[i] != 1:
        for j in range(2, num[i]):
            if num[i]%j == 0 :
                measure.append(j)
        if len(measure) == 0 :
            count += 1
print(count)