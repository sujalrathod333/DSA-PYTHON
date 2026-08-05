#1791 find center of star grapgh

class Solution:
    def findCenter(self, edge: List[List[int]]) -> int:
        if edge[0][0] in edge[1]:
            return edge[0][0]
        return edge[0][1]
