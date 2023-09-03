from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arr_sum = sum(arr)
        equal_sum = arr_sum / 3
        non_empty_parts = 0
        sum_of_elements = 0
        for _, arr_element in enumerate(arr):
            sum_of_elements += arr_element
            if sum_of_elements == equal_sum:
                non_empty_parts += 1
                sum_of_elements = 0
        print(f'non_empty_parts are: {non_empty_parts}')
        return non_empty_parts >= 3

def main():
    s = Solution()
    arr = [0, 0 , 0, 0]
    print(s.canThreePartsEqualSum(arr))
if __name__ =='__main__':
    main()