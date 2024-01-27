x = int(input())
num_list = []
for _ in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for _ in range(len(num_list)):
    print(num_list1[_])