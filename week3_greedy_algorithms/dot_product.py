def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    print(f"len of first sequence is: {len(first_sequence)}")
    print(f"len of second sequence is: {len(second_sequence)}")
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    for i in range(len(first_sequence)):
        max_product += first_sequence[i] * second_sequence[i]

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
