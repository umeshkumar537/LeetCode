class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store the indices of the elements
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]  # Return the indices of the two numbers
            seen[num] = i

# Create an instance of the Solution class and call the method
solution = Solution()

# Test cases
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
