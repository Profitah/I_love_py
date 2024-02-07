A, B = map(int, input().split())

minA = int(str(A).replace('6', '5'))
minB = int(str(B).replace('6', '5'))

maxA = int(str(A).replace('5', '6'))
maxB = int(str(B).replace('5', '6'))

min_sum = minA + minB
max_sum = maxA + maxB

print(min_sum, max_sum)
