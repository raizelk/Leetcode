'''
we have an integer array nums and a we need to remove an int (val) from it and return the number of elements in nums after removing val
we can simply iterate through it once, since lists are mutable we modify the element in it.
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
# 32 ms and 16.41 MB
