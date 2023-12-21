n = int(input())

line = []
if n != 1 and n != 4:
    line.append(" * * *")
else:
    line.append("")
if n != 1 and n != 2 and n != 7 and n != 3:
    for i in range(1, 4):
        line.append("*")
else:
    for i in range(1, 4):
        line.append(" ")
if n != 5 and n != 6:
    for i in range(1, 4):
        line[-i] += "     *"
line.append("")
if n != 0 and n != 1 and n != 7:
    line[-1] += " * * *"
if n == 0 or n == 2 or n == 6 or n == 8:
    for i in range(1, 4):
        line.append("*")
else:
    for i in range(1, 4):
        line.append(" ")
if n != 2:
    for i in range(1, 4):
        line[-i] += "     *"
if n != 1 and n != 4 and n != 7:
    line.append(" * * *")

print("\n".join(line))
