# Robot bounded in circle
# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        mov = [0 for _ in range(4)]  # north,east, south, west
        ind = 0

        for loop in range(4):
            for x in instructions:
                if x == 'G':
                    mov[ind] = mov[ind] + 1
                elif x == 'L':
                    ind = (ind - 1) % 4
                else:
                    ind = (ind + 1) % 4
            if mov[0] == mov[2] and mov[1] == mov[3]:
                return True
        return False
