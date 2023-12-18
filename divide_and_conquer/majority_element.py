def majority_element(elements):
    length_of_list = len(elements)
    elements_d = {}
    count = 0 
    for items in elements:
        elements_d[items] = elements_d.get(items, 0) + 1
        if elements_d[items] > 0:
            count = elements_d[items]
        if count > length_of_list // 2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    input_elements.sort()
    print(majority_element(input_elements))
