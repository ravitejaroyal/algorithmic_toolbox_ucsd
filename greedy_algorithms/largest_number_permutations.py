from itertools import permutations

def is_max(number, max_number):
    return int(max_number + number) <= int(number + max_number)

def largest_number(numbers):
    largest = ''
    while numbers:
        max_number = '0'
        for number in numbers:
            if is_max(number, max_number):
                max_number = number
        largest += max_number
        numbers.remove(max_number)
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))