T = int(input())
x = []
y = []
member = 0
for n in range(T):
    a = int(input)
    b = int(input)
    for i in range(1,b+1):
        x.append(i)
    for j in range(a):
        for k in range(0,b):
            member +=x[k]
            y.append(member)
            x[k] = y[k]
        if i == (a-1):
            continue
        elif i != (a-1):
            y.clear()
            member = 0
    print(x[b-1])