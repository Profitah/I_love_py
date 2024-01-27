import sys
r = sys.stdin.readline

def inside(w, h, rx, ry, px, py):
    if (rx <= px <= rx + w) and (ry <= py <= ry + h):
        return True

    R = h / 2
    d1 = ((px - rx)**2 + (py - (ry + R))**2)**0.5
    d2 = ((px - (rx + w))**2 + (py - (ry + R))**2)**0.5
    if d1 <= R or d2 <= R:
        return True

    return False

def main():
    w, h, rx, ry, n = map(int, r().split())
    c = 0
    for _ in range(n):
        px, py = map(int, r().split())
        if inside(w, h, rx, ry, px, py):
            c += 1
    print(c)

main()
