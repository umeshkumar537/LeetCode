class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Determine the sign
        sign = 1
        index = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            index += 1

        # Step 3: Read the digits
        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        # Apply the sign
        num *= sign

        # Step 4: Clamp the result within the 32-bit integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
