from sys import stdin


def maximum_gold(weights, capacity):
        n = len(capacity)
        dp = [[ 0 for _ in range( weights+1 )] for _ in range( n+1 )]
        for i in range( 1, n+1 ):
            for j in range( 1, weights+1 ):
                if 0 <= j - capacity[ i-1 ]:
                    dp[ i ][ j ] = max( capacity[ i-1 ] + dp[ i-1 ][ j - capacity[ i-1 ]], dp[ i-1 ][ j ] )
                else:
                    dp[ i ][ j ] = dp[ i-1 ][ j ]
        return dp[n][weights]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
