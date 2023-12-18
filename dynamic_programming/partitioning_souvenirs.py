from sys import stdin


def partition3(values):
    n = len(values)
    s=i=j=0
    for i in range(n): s+=values[i]
    if s%3!=0: return False
    part=[[True for i in range(n+1)]for j in range (s//3+1)]
    
    for i in range(0,n+1): 
        part[0][j]=True
    for i in range(1,s//3+1): 
        part[i][0]=False
    for i in range(1,s//3+1):
        for j in range(1,n+1):
            part[i][j]=part[i][j-1]
            if i >=values[j-1]:
                part[i][j]=(part[i][j] or part[i-values[j-1]][j-1])
                
    return(part[s//3][n])

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # input_values = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
    print(int(partition3(input_values)))
