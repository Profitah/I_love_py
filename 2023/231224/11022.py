# 테스트 케이스의 개수 T를 입력받음
t = int(input())

# 1부터 T까지 반복하면서 테스트 케이스를 처리.
for i in range(1, t + 1):
    # a와 b를 입력받습니다.
    a, b = map(int, input().split())
    
    # 결과를 출력합니다. Case #i: a + b = a + b 형식으로 출력.
    print(f"Case #{i}: {a} + {b} = {a + b}")
