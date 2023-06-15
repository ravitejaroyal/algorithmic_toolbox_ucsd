def fibonacci_number(n, m):
    previous = 0
    current = 1
    for _ in range(n-1):
        tmp = previous
        previous =  current
        current = (tmp + current) % 10
    return current % m


if __name__ == "__main__":
    input_i = map(int, input().split())
    n, m = input_i
    print(fibonacci_number(n, m))
