#https://leetcode.com/problems/set-mismatch/submissions/1909462830/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repetido = sum(nums) - sum(set(nums))
        esperado = n*(n+1) //2
        perdido = esperado - sum(set(nums))

        return repetido,perdido
        
