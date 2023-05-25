def fibonacci_number(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n-1):
        previous, current = current, previous + current
    return current % m


if __name__ == "__main__":
    input_i = map(int, input().split())
    n, m = input_i
    print(fibonacci_number(n, m))