import sys
input = sys.stdin.read

data = input().split("\n")
index = 0

T = int(data[index])
index += 1
results = []

for _ in range(T):
    index += 1  
    N, M = map(int, data[index].split())
    index += 1

    cIQ = list(map(int, data[index].split()))
    index += 1

    eIQ = list(map(int, data[index].split()))
    index += 1

    cSum = sum(cIQ)
    eSum = sum(eIQ)

    answer = 0

    for j in range(N):
        if cSum > cIQ[j] * N and eSum < cIQ[j] * M:
            answer += 1

    results.append(answer)

for result in results:
    print(result)
