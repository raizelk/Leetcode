'''
here we need to add 1 to a large number that is written as an array
so we get to cases while in the loop 
the digit is 9 then we change it to zero and add it to preceding digit
if != 9 then we simply add one to the digit
one of my test cases failed because i did not think of the edge case where all the numbers are 9 in that case we need to add a 1 in the beginning of the array
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
