n = int(input())  # 사람 수 입력
peoples = sorted(map(int, input().split()))  # 기다리는 사람들 입력 및 정렬

answer = sum(sum(peoples[:x]) for x in range(1, n+1))  # 누적된 합 구하기
print(answer)  # 정답 출력
