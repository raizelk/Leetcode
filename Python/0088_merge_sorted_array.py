'''
a straight forward problem
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(1,len(nums2)+1):
            index = m-1+i
            nums1[index] = nums2[i-1]
        nums1.sort()
# now good dsa solvers should not use inbuilt functions so we'll do it again
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, index = m-1, n-1, m+n-1
        while j>=0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
#Code1 34 ms Beats 88.41% 
#Code2 40 ms Beats 54.13%
