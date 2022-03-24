N = int(input())
def hanoi(n,start,end) :
    if n == 1 :
        print(start, end)
    else :
        hanoi(n-1, start, 6-start-end)
        print(start,end)
        hanoi(n-1, 6-start-end, end)
sum = 1
for i in range(N-1):
    sum = sum * 2 + 1
print(sum)
hanoi(N,1,3)