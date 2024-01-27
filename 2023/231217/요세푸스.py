n, k = map(int, input().split())
people = [i for i in range(1, n + 1)]  # 맨 처음에 원에 앉아있는 사람들

removed_people = []  # 제거된 사람들을 넣을 배열
index = 0  # 제거될 사람의 인덱스 번호

for _ in range(n):
    index += k - 1  
    if index >= len(people):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        index = index % len(people)
 
    removed_people.append(str(people.pop(index)))

print("<", ", ".join(removed_people)[:], ">", sep='')
