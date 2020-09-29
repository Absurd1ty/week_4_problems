"""Given the array of integers nums, you will choose two 
different indices i and j of 
that array. Return the maximum 
value of (nums[i]-1)*(nums[j]-1)."""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        nums.sort()
        max_product = (nums[-1] -1) * (nums[-2] -1)
        return max_product