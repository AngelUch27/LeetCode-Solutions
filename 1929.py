#https://leetcode.com/problems/concatenation-of-array/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i) 
        return ans  