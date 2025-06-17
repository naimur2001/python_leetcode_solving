# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        maxReach=0
        jumpCounter=0
        lastIndex=0

        for i in range(len(nums)):
          
            maxReach=max(maxReach,i+nums[i])
            if i==lastIndex:
             jumpCounter+=1
             lastIndex=maxReach
             if maxReach>=len(nums)-1:
                return jumpCounter
               

          
        return jumpCounter

                
       
           
    
    
s=Solution()
print(s.jump([2,3,0,1,4]))
# print(s.jump([2,1]))