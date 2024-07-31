'''
This is the first problem I struggled in...
The brute force way would be to obviously make three for loops with time complexity O(n^3)
since this array allows duplicates i was concerned about repeating results, so I thought of using sets but then i quickly realised the possibility of (-1, -1, 2).
I then started studying solutions on leetcode and came across this wonderful solution https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return[]

        res = set()
        n,p,z = [], [], []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
        #In the above block of code we have split nums into 3 lists of positive(p), negative(n) and zeros(z)
        N, P = set(n), set(p) #We constructed set of the lists n and p for O(1) lookup times to avoid duplicate in needed cases
        #for cases like (-2,0,2)
        if z:
            for num in P: #here P and N are sets hence no duplicates
                if -1*num in N: #(-1*2 = -2 in N)
                    res.add((-1*num,0,num))
        
        #(0,0,0)
        if len(z) >= 3:
            res.add((0,0,0))
        
        #positive complement
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        
        #negative complemet
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
        
        return res
#514 ms and 21.11 MB
'''
Upon pondering some more since even though the run time is better than 97% the memory is only at 12.89, to optimize it i thought of sorting the array choosing a number and then using two pointer.
The time complexity should remain O(n^2) { O(nlogn) + O(n^2)}
I can even use the enumerate() in python it returns (obj,indice of obj)
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a > 0:
                break #to skip positive numbers
            
            if i > 0 and a == nums[i - 1]:
                continue #to check if previous element is equal
            
            #now on the sorted array we can use three pointer like in two sum 2
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
#509ms (beating 97.5%) and 20.7 MB (beating 65.34%)
#the runtime is similar beacuse the time complexity for both is O(n^2) but this method uses less space





