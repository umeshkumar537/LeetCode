from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        chars = ['a', 'b', 'c']
        happy_strings = sorted(["".join(p) for p in product(chars, repeat=n) if is_happy("".join(p))])
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

# Example test cases
sol = Solution()
print(sol.getHappyString(1, 3))  # Output: "c"
print(sol.getHappyString(1, 4))  # Output: ""
print(sol.getHappyString(3, 9))  # Output: "cab"
