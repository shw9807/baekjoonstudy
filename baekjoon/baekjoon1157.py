word = input().upper()
answer = []
max_count = 0
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
    if word.count(i) > max_count:
        answer = []
        answer.append(i)
        max_count =word.count(i)
    elif word.count(i) == max_count :
        answer.append(i)
if len(answer) == 1:
    print(answer[0])
else :
    print('?')