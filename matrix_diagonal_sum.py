"""Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary 
diagonal and all the elements on the secondary 
diagonal that are not part of the primary diagonal."""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        numbers = len(mat)
        sum = 0
        
        for i in range(numbers):
            sum = sum + mat[i][i]
            sum = sum + mat[i][numbers-i-1]


        if numbers %2 == 1:
            sum = sum - mat[numbers // 2][numbers // 2]

        return sum