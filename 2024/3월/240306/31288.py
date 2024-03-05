def sol(n, num):
    if n == 1:
        return "4 2"
    rem = sum(int(c) for c in num) % 3
    ans = []
    for i in range(n):
        x = int(num[i])
        nx = x - rem
        nx += 3 if nx <= 0 else 0
        ans.append(f"{num[:i]}{nx}{num[i+1:]} 3")
    return "\n".join(ans)

if __name__ == "__main__":
    import sys

    N = int(sys.stdin.readline().strip())
    Sb = []
    for _ in range(N):
        m, s = sys.stdin.readline().strip().split()
        Sb.append(sol(int(m), s))
    print("\n".join(Sb))
