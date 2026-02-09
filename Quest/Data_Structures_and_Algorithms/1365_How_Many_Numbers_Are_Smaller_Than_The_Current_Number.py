#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            contador = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j != i:
                    contador+=1 
            res[i] = contador

        return res
