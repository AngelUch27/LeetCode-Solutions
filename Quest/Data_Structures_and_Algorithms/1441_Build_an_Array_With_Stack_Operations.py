# Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/?# envType=problem-list-v2&envId=dsa-linear-shoal-stack
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        array = []
        aux = 1
        
        for i in range(len(target)):
            t = target[i]
            while aux < t:
                array.append("Push")
                array.append("Pop")
                aux += 1

            array.append("Push")
            aux += 1

        return array
