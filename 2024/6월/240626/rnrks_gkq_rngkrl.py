import sys
input = sys.stdin.read

def solution():
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    
    arr = list(map(int, data[2:m+2]))
    queries = data[m+2:]
    
    prefix_sum = [0] * (m + 1)
    
    for i in range(1, m + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    results = []
    for i in range(n):
        a = int(queries[2 * i])
        b = int(queries[2 * i + 1])
        results.append(str(prefix_sum[b] - prefix_sum[a - 1]))
    
    print("\n".join(results))

if __name__ == "__main__":
    solution()