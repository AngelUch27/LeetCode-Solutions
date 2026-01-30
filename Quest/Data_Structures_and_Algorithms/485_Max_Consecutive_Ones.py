#Q3
# https://leetcode.com/problems/max-consecutive-ones/submissions/1902280965/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        contador = 0
        maximo = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                contador+=1
            if contador > maximo:
                    maximo = contador
            if nums[i] == 0:
                contador = 0
        return maximo
