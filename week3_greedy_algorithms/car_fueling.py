from sys import stdin


def min_refills(distance, tank, stops):

    # no need to fill the tank
    if distance < tank:
        return 0
    # can't reach the gas station
    i = 0
    min_stops = 0

    while i < len(stops) - 1:
        if tank < stops[0] or stops[i + 1] - stops[i] > tank:
            return -1
        if tank < stops[i]:
            min_stops += 1
            distance -= tank
            tank += stops[i-1]
        if tank == stops[i]:
            min_stops += 1
            distance -= tank
            tank += stops[i]
        i += 1

    return min_stops


if __name__ == '__main__':
    d, m, n_stops = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    print(min_refills(d, m, stops))
