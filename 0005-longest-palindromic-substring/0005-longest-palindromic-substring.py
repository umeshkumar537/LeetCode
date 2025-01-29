class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> int:
            # Expand as long as the characters on both sides are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length of the palindrome

        if len(s) <= 1:
            return s

        start, max_len = 0, 0
        for i in range(len(s)):
            # Check for odd-length palindromes
            len1 = expand_around_center(i, i)
            # Check for even-length palindromes
            len2 = expand_around_center(i, i + 1)
            # Get the maximum length
            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]
