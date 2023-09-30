def fibonacci_number(m, n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 0
    for i in range(n-1):
        previous, current = current, previous + current
        if i >= m - 2:
            sum += current
    return sum % 10

if __name__ == "__main__":
    m, n = map(int, input().split())
    print(fibonacci_number(m, n))
