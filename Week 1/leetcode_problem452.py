# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        cur=points[0]

        count=1
        for x in points:
            if x[0]>cur[1]:
                count+=1
                cur=x
        return count