
def lcs3(a, b, c):
    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    matrix = [[[float("-inf")] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            for k in range(n3 + 1):
                if i == 0 or j == 0 or k == 0:
                    matrix[i][j][k] = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1], matrix[i - 1][j - 1][k], matrix[i - 1][j][k - 1], matrix[i][j - 1][k - 1])
    return matrix[n1][n2][n3]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
