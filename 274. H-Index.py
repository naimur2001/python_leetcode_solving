# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# If there are several possible values for h, the maximum one is returned.

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
            return 0
        count=0
        for i in range(len(citations)):
            if citations[i]>1000:
                return 0
            if citations[i]>=3 or len(citations)==1:
                count=count+1
        return count
            
  # elif citations[i]!=3 and citations[i]>0  :
  #                   count=count+1        
  #                   return count

s=Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([1,3,1]))
print(s.hIndex([1]))
print(s.hIndex([0,0,2]))
print(s.hIndex([1,2,2]))
         