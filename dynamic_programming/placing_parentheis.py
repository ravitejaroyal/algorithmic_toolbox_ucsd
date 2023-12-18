import math
    
def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(M, m, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], operators[k])
        b = evaluate(M[i][k], m[k+1][j], operators[k])
        c = evaluate(m[i][k], M[k+1][j], operators[k])
        d = evaluate(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def maximum_value(dataset):
    operators, operands = [], []
    for i in dataset:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))
        
    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input()))
