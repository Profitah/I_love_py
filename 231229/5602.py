def main():
    n, m = map(int, input().split())
    column = [0] * m

    for _ in range(n):
        row = list(map(int, input().split()))
        column = [count + r for count, r in zip(column, row)]

    sorted_columns = sorted(range(1, m + 1), key=lambda x: column[x - 1], reverse=True)
    print(*sorted_columns)

if __name__ == "__main__":
    main()
