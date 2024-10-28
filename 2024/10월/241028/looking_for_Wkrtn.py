num_test_cases = int(input())

for _ in range(num_test_cases):
    user_input_values = list(map(int, input().split()))  
    evens = [value for value in user_input_values if value % 2 == 0]  
    
    print(sum(evens), min(evens))
