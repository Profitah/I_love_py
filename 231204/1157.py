# 질문게시판 참고
# 사용자로부터 문자열을 입력받고 대문자로 변환하여 변수에 저장
n = input().upper()

# 문자열의 각 문자를 집합으로 변환하여 중복을 제거
ns = set(n)

# 각 문자의 등장 횟수를 세어 사전에 저장
ans = {}
for i in ns:
    ans[i] = n.count(i)

# 등장 횟수가 가장 많은 문자를 찾음
maxl = [k for k, v in ans.items() if max(ans.values()) == v]

# 등장 횟수가 가장 많은 문자가 1개일 경우 출력, 그 외에는 "?" 출력
if len(maxl) == 1:
    print(*maxl)
else:
    print("?")
