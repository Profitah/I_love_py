# 숫자 카드의 개수를 세는 함수 정의
def count_cards(cards, nums_to_find):
    # 각 카드가 몇 개씩 있는지 저장할 딕셔너리 초기화
    card_count = {}
    
    # 모든 카드에 대해
    for card in cards:
        # 해당 카드의 개수를 1 늘림 (카드가 없다면 0에서 1 늘림)
        card_count[card] = card_count.get(card, 0) + 1
    
    # 찾아야 하는 숫자들이 몇 개씩 있는지 리스트로 반환
    return [card_count.get(num, 0) for num in nums_to_find]

# 사용자로부터 숫자 카드의 개수를 입력받음
n = int(input())

# 사용자로부터 숫자 카드를 입력받음
cards = list(map(int, input().split()))

# 사용자로부터 찾아야 하는 숫자의 개수를 입력받음
m = int(input())

# 사용자로부터 찾아야 하는 숫자들을 입력받음
nums = list(map(int, input().split()))

# 함수를 호출하여 찾아야 하는 숫자들이 몇 개씩 있는지 계산
result = count_cards(cards, nums)

# 결과 출력
print(*result)
