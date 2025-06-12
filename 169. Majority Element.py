# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#        Final advice:
# Use the Boyer-Moore code above.

# Don’t sort — sorting is O(n log n), slower than linear.

# Don’t count repeatedly in loops.
        nums.sort()
        canditate=None
        count=0
        for i in nums:

            if count==0:
                canditate=i

            if canditate==i:
                count+=1
            else:
                count-=1
        

  
        return canditate        
         
        
            
            
          


s=Solution()

# print(s.majorityElement([2,2,1,1,1,1,1,1,1,2,2]))
print(s.majorityElement([3,8,8,6]))

         
        