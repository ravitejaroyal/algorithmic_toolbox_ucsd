
def fibonacci_number(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        previous, current = current, previous + current
    last_digit = current % 10
    return last_digit

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))