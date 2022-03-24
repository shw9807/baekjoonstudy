n = int(input())
def pibo(n):
    d = [0]*21
    sum = 0
    if n == 0 :
        return 0
    elif n == 1 or n == 2 :
        return 1
    elif d[n] !=0:
        return d[n]
    
    d[n] = pibo(n-1)+pibo(n-2)
    return d[n]

print(pibo(n))