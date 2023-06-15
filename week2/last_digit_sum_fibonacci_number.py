def fibonacci_number(n):
    previous = 0
    current = 1
    for _ in range(n-1):
        tmp = previous
        previous =  current
        current = (tmp + current) % 10
        sum += current
    return sum % 10

if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
