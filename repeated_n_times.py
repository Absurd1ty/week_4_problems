"""In a array A of size 2N, there are N+1 unique elements, 
and exactly one of these elements is repeated N times.

Return the element repeated N times."""


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return mode(A)


""" Clever solutuion :)"""