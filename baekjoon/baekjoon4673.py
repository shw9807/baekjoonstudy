def selfnum():
    result = []
    n = 0
    while n != 10000:
        for i in range(1, 10001) :
            a = [int(b) for b in str(i)]
            sumi = i + sum(a)
            result.append(sumi)
        for i in range(1, 10001):
            n = n + 1
            if i in result:
                pass
            else:
                print(i)
selfnum()