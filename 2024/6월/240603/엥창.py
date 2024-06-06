import math

def can_pass_through_hole(match_length, max_length):
    return "DA" if match_length <= max_length else "NE"

def main():
    N, W, H = map(int, input().split())
    
    max_length = math.sqrt(W**2 + H**2)
    
    results = [can_pass_through_hole(int(input()), max_length) for _ in range(N)]
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
