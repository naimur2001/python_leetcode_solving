# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        return nums

  
s1=Solution()
print(s1.rotate([1,2,3,4,5,6,7],3))


