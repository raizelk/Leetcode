'''
How is it different from two sum (1) - 1. The array is sorted, 2. We need to return the indice+1 
hence instead of a for loop that we used previously we can use two-pointer method because we know that,
if the corner most point l + r == target then it is ok,
if l + r < target we can move l towards right increasing the sum and checking again or l + r > target we can move r towards l to decrease the sum
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l +=1
            else:
                r -= 1
#101 ms and 17.73MB
