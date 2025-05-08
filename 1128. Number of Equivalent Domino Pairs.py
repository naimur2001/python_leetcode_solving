# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3

from typing import List



class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        check=0
        for i in range(len(dominoes)):
            for j in range(i+1,len(dominoes)):
               if sorted(dominoes[i])==sorted(dominoes[j]):
                   check=check+1
 
        return check

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]

s=Solution()
print(s.numEquivDominoPairs(dominoes))


# from collections import defaultdict

# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         count = 0
#         freq = defaultdict(int)  # Create an empty hashmap with default 0

#         for a, b in dominoes:
#             key = tuple(sorted((a, b)))  # Normalize: (1,2) and (2,1) become (1,2)
#             count += freq[key]           # Add how many times we've seen this pair before
#             freq[key] += 1               # Update frequency in the hashmap

#         return count
