x = int(input())
lists = input()

count = lists.count('LL')

if (count <= 1):
    print(len(lists))

else:
    print(len(lists) - count + 1)
