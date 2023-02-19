import pdb
def max_pairwise_product(numbers):
    n = len(numbers)
    max_index1 = -1
    # find first maximum number
    for i in range(n):
        if (max_index1 == -1 or numbers[i] > numbers[max_index1]):
            max_index1 = i

    max_index2 = -1
    for j in range(n):
        if ((max_index1 != j) and (max_index2 == -1 or numbers[j] > numbers[max_index2])):
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
    