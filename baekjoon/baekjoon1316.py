N = int(input())
count = 0
for _ in range(N):
    word = input()
    list = []
    for i in len(word):
        if word[i] not in list:
            list.append(word[i])
        elif word[i] in list :
            if word[i] == word[i-1] :
                list.append(word[i])
    if len(list) == len(word) :
        count += 1
print(count)