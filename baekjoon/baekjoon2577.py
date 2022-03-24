a = int(input())
b = int(input())
c = int(input())
multi = str(a*b*c)
x = [0 for x in range(10)]
for i in range(10):
    x[i] = multi.count(str(i))
    print(x[i])