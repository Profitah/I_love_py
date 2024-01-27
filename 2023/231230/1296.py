if __name__ == '__main__':
    # 기준 문자열 ms를 입력받음
    ms = input()
    # 단어의 개수 n을 입력받음
    n = int(input())
    # 단어 리스트 w_list를 입력받고 정렬
    w_list = sorted([input() for i in range(n)])

    # 최대 확률과 그에 해당하는 인덱스를 초기화
    max_p = max_i = 0

    # 단어 리스트의 각 단어에 대해 반복
    for i in range(n):
        # 각 알파벳의 개수를 세어 변수에 저장
        L = ms.count('L') + w_list[i].count('L')
        O = ms.count('O') + w_list[i].count('O')
        V = ms.count('V') + w_list[i].count('V')
        E = ms.count('E') + w_list[i].count('E')

        # 확률을 계산
        p = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

        # 현재 확률이 최대 확률보다 큰 경우 최대 확률과 인덱스를 갱신
        if p > max_p:
            max_p = p
            max_i = i

    # 최대 확률에 해당하는 단어를 출력
    print(w_list[max_i])
