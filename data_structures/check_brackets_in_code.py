# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    count = 0
    top = -1
    for i, next in enumerate(text):
        count = count + 1
        if next in "([{":
            top = top + 1
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, count))

        if next in ")]}":
            # corner case: starting one is closed bracket
            if len(opening_brackets_stack) == 0:
                return i + 1
            
            # Process closing bracket, write your code here
            if are_matching(opening_brackets_stack[top][0], next):
                opening_brackets_stack.pop()
                # opening_brackets_stack.remove(opening_brackets_stack[top])
                top = top - 1
            else:
                return count
            
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[top][1]
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
