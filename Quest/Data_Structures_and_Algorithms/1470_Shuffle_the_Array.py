# Q2
# https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffleado = []
        for i in range(n):
            shuffleado.append(nums[i])
            shuffleado.append(nums[n+i])
        return shuffleado


        
