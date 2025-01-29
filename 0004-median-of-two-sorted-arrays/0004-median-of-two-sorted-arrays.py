class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            # Directly compute max and min for partitions
            maxX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minX = nums1[partitionX] if partitionX < m else float('inf')
            maxY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minY = nums2[partitionY] if partitionY < n else float('inf')

            # Check if correct partition is found
            if maxX <= minY and maxY <= minX:
                # Median calculation for even and odd combined
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                return max(maxX, maxY)
            elif maxX > minY:
                # Move search window to the left
                right = partitionX - 1
            else:
                # Move search window to the right
                left = partitionX + 1

        raise ValueError("Input arrays are not sorted.")  # Should never happen with valid input

# Example usage
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))        # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))     # Output: 2.5
print(solution.findMedianSortedArrays([0, 0], [0, 0]))     # Output: 0.0
print(solution.findMedianSortedArrays([], [1]))            # Output: 1.0
print(solution.findMedianSortedArrays([2], []))            # Output: 2.0
