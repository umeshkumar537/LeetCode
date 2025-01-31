class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Handle negative numbers by remembering the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits of x
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        # Apply the original sign to the reversed number
        reversed_x *= sign
        
        # Check if the reversed number is within the 32-bit integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x

# Example Usage
solution = Solution()
print(solution.reverse(123))  # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))  # Output: 21
print(solution.reverse(0))  # Output: 0
