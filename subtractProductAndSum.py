class Solution:
    def subtractProductAndSum(self, n: int) -> int:
         product = 1
         total = 0
        
         for digit in str(n):
            product *= int(digit)
            total += int(digit)
            
         return product - total