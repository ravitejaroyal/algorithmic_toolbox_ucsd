def fibonacci_number(m, n):
    n = n % 60
    if n <= 1:
        return n
    previous = 0
    current = 1
    if m > 2:
        sum = 0
    else:
        sum = 1
    for i in range(n-1):
        tmp = previous
        previous =  current
        current = (tmp + current) % 10
        if i >= m - 2:
            sum = (sum + current) % 10
    return sum

if __name__ == "__main__":
    m, n = map(int, input().split())
    print(fibonacci_number(m, n))
