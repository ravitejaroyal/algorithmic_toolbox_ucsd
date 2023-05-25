
def fibonacci_number(n):
    if n <= 1:
        return n
    total = fibonacci_number(n-2) + fibonacci_number(n-1)
    last_digit = total % 10
    return last_digit

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))