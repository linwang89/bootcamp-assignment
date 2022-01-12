# Add Binary
# https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0':
            return b
        if b == '0':
            return a

        aa = int(a)
        bb = int(b)
        cc = aa + bb
        res = ''
        digit = 10
        while digit / 10 < cc:
            if (cc % digit) / (digit / 10) >= 2:
                cc = cc + digit - 2 * digit / 10
            digit = digit * 10
        return str(cc)
