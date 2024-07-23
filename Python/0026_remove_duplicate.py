'''
here we have an array in increasing order with duplicates
we need to return the number of unique elements k and Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially
That means the array nums must be modified itself with the same relative length
'''
# I came up with a simple loop to modify num and pass through it
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1
# 76 ms and 17.95 MB 
