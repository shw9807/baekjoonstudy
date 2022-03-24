m = n = int(input())
i=2
j=0
x = []
while i < n//2+1 :
    if m%i == 0 :
        x.append(i)
        print(x[j])
        m = m//i
        j += 1
    else :
        i += 1
if m == 1:
    pass
elif len(x) == 0:
    print(n)