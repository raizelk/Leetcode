'''
Here, we need to add two numbers in a list/array called nums such that it matches the target and returns the indices from nums.
With two conditions:
1. Exactly one solution 
2. Not passing through same element twice
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return ([i,j])
#run time of 1650 ms and memory usage of 17.14 MB
#O(n^2) ordered time complexity can be avoided using dictionaries
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
#run time of 47 ms and memory usage of 17.76 MB
