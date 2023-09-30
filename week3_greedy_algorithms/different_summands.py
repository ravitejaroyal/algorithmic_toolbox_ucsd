def optimal_summands(n):
    summands = []
    # write your code here
    if n == 2:
        summands.append(2)
        return summands
    i = 1
    while n > 0:
        n_orig = n
        n = n - i # 8 --> 8 -1 = 7 ---> 7 - 2 = 5 ---> 5 - 3 = 2 but 2 is in summands so append 5 to summands and break
        if n not in summands:
            summands.append(i)
        else:
            summands.append(n_orig)
            break
        i = i + 1
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
