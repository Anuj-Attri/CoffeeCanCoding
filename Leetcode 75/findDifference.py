'''
2215. Find the Difference of Two Arrays
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''

'''
Gist:
Python lists do not support '-' operand, hence type-casting to set is executed.
Sets have an O(1) lookup time, making the program extremely efficient.

The unique elements of nums1 are found by subtracting nums2 from it, and vice versa.
Multiple type-castings are avoided for optimization reasons, by converting the lists to sets before the operation.

Time: O(N + M) => O(K)
Space: O(N + M) => O(K)
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]