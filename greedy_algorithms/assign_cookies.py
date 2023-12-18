from typing import List
# g is greed factor of children, s is size of cookies
# Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        max_number, i, j = 0, 0, 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                i += 1
                j += 1
                max_number += 1
            else:
                i += 1
        return max_number

def main():
    s= Solution()
    greed_factor_for_children = [7, 8, 9, 10]
    size_of_the_cookies = [5, 6, 7, 8]
    print(s.findContentChildren(greed_factor_for_children, size_of_the_cookies))

if __name__ == '__main__':
    main()