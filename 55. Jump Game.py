# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum=0
        for i in range(len(nums)):
            if i>maximum:
                return False
            if i+nums[i]>maximum:
                maximum=i+nums[i]
        return True
    
s=Solution()
print(s.canJump([3,2,1,0,4]))