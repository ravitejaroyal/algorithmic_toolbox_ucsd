from typing import List
from typeguard import typechecked

@typechecked
class Solution:
    def maximum_units(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        output = 0
        i = 0
        j = 0
        length_of_box_types = len(boxTypes)
        while truckSize > 0 and length_of_box_types > 0:
            if boxTypes[i][j] <= truckSize:
                output += boxTypes[i][j] * boxTypes[i][j+1]
                truckSize -= boxTypes[i][j]
                i = i + 1
                length_of_box_types -= 1
            else:
                output += truckSize * boxTypes[i][j+1]
                truckSize = 0
        return output

def main():
    s = Solution()
    box_types = [[5,10],[2,5],[4,7],[3,9]]
    truck_size = 10
    print(s.maximum_units(box_types, truck_size))

if __name__ == '__main__':
    main()