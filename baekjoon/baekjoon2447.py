import math

N = int(input())
Input_list = [ 3**i for i in range(1,8)]
Result = [[" " for i in range(N)] for j in range(N)]
def Make(N, x, y):
    N = N / 3
    if N == 1:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    Result[int(x + i)][int(y + j)] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                Make(N, x + N * i, y + N * j)

if Input_list.count(N) > 0:
    Make(N, 0 ,0)
    for i in range(N):

        print("".join(Result[i]))
else:
    pass