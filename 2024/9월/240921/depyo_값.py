import statistics

int1 = int(input())
int2 = int(input())
int3 = int(input())
int4 = int(input())
int5 = int(input())
int6 = int(input())
int7 = int(input())
int8 = int(input())
int9 = int(input())
int10 = int(input())

intlist = [int1, int2, int3, int4, int5, int6, int7, int8, int9, int10]
intsum = sum(intlist)

print(intsum // 10)
print(statistics.mode(intlist))


# for i in range(10):
#     intlist.append(int(input()))
# 으로 사용자 입력을 보다 효율적으로 받을 수 있다는 것을 알고 있지만
# 그렇게 풀고 싶은 기분이 아니여서 이렇게 했다. 