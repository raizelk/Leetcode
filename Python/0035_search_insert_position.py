'''
a simple binary search problem since it is given we must write a program at O(log n) time complexity. 
i thought of making a left (l) and right(r) that would be index len(nums)-1 after that we can take the mid we might find the solution at the first try if the target == mid
if not we move towards the left and repeat the search
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0 ,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
# 15 ms 17.2 MB
