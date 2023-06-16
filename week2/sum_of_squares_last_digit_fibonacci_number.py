def fibonacci_number(n):
    n = n % 60
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1
    for _ in range(n-1):
        tmp = previous
        previous =  current
        current = (tmp + current) % 10
        sum  = (sum + (current * current)) % 10
    return sum

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
