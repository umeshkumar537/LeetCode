class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there is only one row or the string is shorter than the number of rows, return the string as is
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate over the string and place characters in appropriate rows
        for char in s:
            rows[current_row] += char
            
            # Change direction if we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row in the appropriate direction
            current_row += 1 if going_down else -1
        
        # Join all rows and return the resulting string
        return ''.join(rows)

# Example Test Cases:
solution = Solution()

print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))              # Output: "A"
