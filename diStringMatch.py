"""Given a string S that only contains "I" 
(increase) or "D" (decrease), 
let N = S.length.

Return any permutation A of [0, 1, ..., N] 
such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        final = list()
        upper_bound = len(S)
        lower_bound = 0
        
        for i in range(len(S)):
            
            if S[i] == "I":
                final.append(lower_bound)
                lower_bound += 1
            
            elif S[i] == "D":
                final.append(upper_bound)
                upper_bound -= 1
            
            if upper_bound == lower_bound:
                final.append(lower_bound)
        
        return final