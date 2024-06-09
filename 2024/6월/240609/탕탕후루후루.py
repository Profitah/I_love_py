## 백준 과일 탕후루 
# 투 포인터와 dp를 이용한 풀이

import sys
input = sys.stdin.read

lstData = input().split()

# 사용자가 입력한 데이터 중 첫 번째 값은 과일의 개수를 나타내는 정수 x로 변환
x = int(lstData[0])

# 나머지 값들은 과일 종류를 나타내는 리스트 lstFruits로 변환
lstFruits = list(map(int, lstData[1:x+1]))

# 두 종류 이하의 과일로 구성된 가장 긴 부분 배열의 길이를 찾는 함수
def findMaxFruitTanghulu(lstFruits):
    xLen = len(lstFruits)  # 과일 리스트의 길이
    xLeft = 0  # 왼쪽 포인터 초기화
    xRight = 0  # 오른쪽 포인터 초기화
    xMaxCount = 0  # 두 종류 이하의 과일로 구성된 가장 긴 부분 배열의 길이
    dictFruit = {}  # 과일 종류와 개수를 저장하는 딕셔너리
    
    # 오른쪽 포인터가 리스트 끝에 도달할 때까지 반복
    while xRight < xLen:
        # 현재 과일이 딕셔너리에 존재하면 개수를 1 증가 
        if lstFruits[xRight] in dictFruit:
            dictFruit[lstFruits[xRight]] += 1
        # 존재하지 않으면 새로운 과일을 딕셔너리에 추가
        else:
            dictFruit[lstFruits[xRight]] = 1
        
        # 과일 종류가 2개를 초과하면 왼쪽 포인터를 이동
        while len(dictFruit) > 2:
            dictFruit[lstFruits[xLeft]] -= 1
            # 개수가 0이 되면 딕셔너리에서 해당 과일을 삭제
            if dictFruit[lstFruits[xLeft]] == 0:
                del dictFruit[lstFruits[xLeft]]
            xLeft += 1  # 왼쪽 포인터를 오른쪽으로 이동
        
        # 현재 구간의 길이만큼 최대 길이를 갱신
        xMaxCount = max(xMaxCount, xRight - xLeft + 1)
        xRight += 1  # 오른쪽 포인터를 오른쪽으로 1칸 이동
    
    return xMaxCount  # 두 종류 이하의 과일로 구성된 가장 긴 부분 배열의 길이를 반환

print(findMaxFruitTanghulu(lstFruits))
