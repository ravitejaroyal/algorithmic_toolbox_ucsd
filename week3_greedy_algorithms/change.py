def change(money):
    denominations = [1, 5, 10]
    change = 0
    while money > 0:
        max_coin = [d for d in denominations if d <= money]
        if len(max_coin) == 0:
            return -1
        money = money - max(max_coin)
        change = change + 1

    return change

if __name__ == '__main__':
    m = int(input())
    print(change(m))