def simple_solution():
    test_cases = int(input())
    for _ in range(test_cases):
        first_input_size = int(input())
        for _ in range(first_input_size):
            input()

        second_input_size = int(input())
        for _ in range(second_input_size):
            input()

        if first_input_size == second_input_size:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    simple_solution()
