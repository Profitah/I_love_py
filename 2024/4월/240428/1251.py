user_input= list(input())
answer = []
tmp = []

for i in range(1, len(user_input) - 1):
    for j in range(i + 1, len(user_input) ):
        w1 = user_input[:i]
        w2 = user_input[i:j]
        w3 = user_input[j:]
        w1.reverse()
        w2.reverse()
        w3.reverse()
        tmp.append(w1 + w2 + w3)

for w1 in tmp:
    answer.append(''.join(w1))

print(sorted(answer)[0])