N = int(input())

print(*['god' + ''.join(input().split()[1:]) for _ in range(N)], sep='\n')
