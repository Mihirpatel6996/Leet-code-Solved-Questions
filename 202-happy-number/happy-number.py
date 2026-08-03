class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_digits(num):
            return sum(int(digit)**2 for digit in str(num))
        
        slow = n
        fast = n
        while (fast != 1):
            slow = sum_of_squares_of_digits(slow)
            fast = sum_of_squares_of_digits(fast)
            fast = sum_of_squares_of_digits(fast)

            if(slow == fast and slow!=1):
                return False         
        return True 

        