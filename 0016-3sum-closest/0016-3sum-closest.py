class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  # Exact match found
        
        return closest_sum

# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(solution.threeSumClosest([0, 0, 0], 1))       # Output: 0
