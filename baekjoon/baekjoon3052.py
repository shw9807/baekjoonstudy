remain = []
for i in range(10):
    remain.append(int(input())%42)
remain = set(remain)
print(len(remain))