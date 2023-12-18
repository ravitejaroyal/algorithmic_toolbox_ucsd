def lcs2(first_sequence, second_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    L = [[None]*(n+1) for i in range(m+1)]
  
    for i in range(m+1):
        for j in range(n+1):
            
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif first_sequence[i-1] == second_sequence[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
  
    return L[m][n]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
