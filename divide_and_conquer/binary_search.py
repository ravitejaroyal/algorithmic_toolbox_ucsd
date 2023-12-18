def binary_search_helper(keys, query, low_index, high_index):
    if low_index > high_index or high_index < low_index:
        return -1
    
    mid_index = (low_index + high_index) // 2
    
    if keys[mid_index] == query:
        return mid_index
    
    if keys[mid_index] > query:
        high_index = mid_index - 1
        mid = binary_search_helper(keys, query, low_index, high_index)

    if keys[mid_index] < query:
        low_index = mid_index + 1
        mid = binary_search_helper(keys, query, low_index, high_index)

    return mid


def binary_search(keys, query):
    # write your code here
    low_index = 0
    high_index = len(keys) - 1

    index_location = binary_search_helper(keys, query, low_index, high_index)
    return index_location

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
