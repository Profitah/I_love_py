for _ in range(2):
    a, b, c, d, e = map(int, input().split())

    total_score = a * 6 + b * 3 + c * 2 + d + e * 2

    print("총 점수", total_score, end=" ")
