'''
we are given array called height with length n. we need to find two heights in which maximum water can be stored.
I initially thought of the brute force approach, with 0(n2) run time. 
using two for loops it sadly was not accepted as it exceeded the time limit
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
      out = 0
      for l in range(len(height)):
        for r in range(l+1,len(height)):
            area = (r-l) * min(height[l],height[r])
            out = max(area,out)
      return out 
#we'll use the two pointer method 
class Solution:
    def maxArea(self, height: List[int]) -> int:
      out = 0
      l , r = 0 , len(height) - 1
      while l < r:
        area = (r-l) * min(height[l],height[r])
        out = max(area,out)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
      return out
