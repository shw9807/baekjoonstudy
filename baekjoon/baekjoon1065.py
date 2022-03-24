n = int(input())
def han(n) :
    if n < 100:
        print(n)
    else:
        count = 99
        for i in range(100, n+1):
            a = i // 100
            b = (i % 100) // 10
            c = i % 10
            if (b - a) == (c - b):
                count += 1
        print(count)
han(n)