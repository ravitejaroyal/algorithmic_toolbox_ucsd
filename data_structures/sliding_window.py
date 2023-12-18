# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    Q = deque()
    for i in range(m):
        while Q and sequence[i] >= sequence[Q[-1]]:
            Q.pop()
        Q.append(i)
    
    for i in range(m, len(sequence)):
        maximums.append(sequence[Q[0]])

        while Q and Q[0] <= i - m:
            Q.popleft()

        while Q and sequence[i] >= sequence[Q[-1]]:
            Q.pop()
        Q.append(i)
    maximums.append(sequence[Q[0]])

    return maximums



if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

