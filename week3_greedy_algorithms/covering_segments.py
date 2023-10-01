import sys
from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key=lambda x: x.end)
    points = []
    # write your code here
    tmp = -1
    for s in segments:
        if tmp < s.start:
            points.append(s.end)
            tmp = s.end
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
