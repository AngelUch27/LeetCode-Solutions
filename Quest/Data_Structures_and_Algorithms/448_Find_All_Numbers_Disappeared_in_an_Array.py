# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1913980797/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
# Q3. Find All Numbers Disappeared in an Array
# 448 Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        nums = set(nums)
        
        for i in range(1,n+1):
            if i not in nums:
                res.append(i)

        return res
