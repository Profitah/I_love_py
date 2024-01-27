g = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
s = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

c, t, ts = 0, 0, 0

for _ in range(20):
    _, cr, gr = input().strip().split()
    cr = float(cr)
    
    if gr != "P":
        idx = g.index(gr)
        sc = s[idx]
        ts += cr * sc
        t += cr

avg_score = ts / t
print(avg_score)
