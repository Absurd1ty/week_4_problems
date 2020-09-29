"""Given an array A of non-negative integers, return an array consisting 
of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition."""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(A)):
            
            if A[i] == 0:
                even.append(A[i])
            
            elif A[i] %2 ==0:
                even.append(A[i])
            
            else:
                odd.append(A[i])
        
        return even + odd
        
        