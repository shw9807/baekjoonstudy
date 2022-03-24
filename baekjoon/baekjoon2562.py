num = []
for _ in range(9):
    x = int(input())
    num.append(x)
index = 0
for i in range(9):
    if num[i] == max(num):
        index = i+1 
print(max(num))
print(index)