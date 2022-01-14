# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign=''
        flag=False#number starts
        flag2=False#sign starts
        flag3=False#0starts
        nums=''
        for x in s:
            if x.isdigit():
                if x=='0':
                    if not flag:
                        flag3=True
                        continue
                nums=nums+x
                flag=True
            elif x==' ':
                if flag or flag2 or flag3:
                    break
            elif x=='-'  or x=='+':
                if flag or flag2 or flag3:
                    break
                sign=x
                flag2=True
            else:
                break
        if not nums:
            return 0
        if sign=='-':
            num=-int(nums)
        else:
            num=int(nums)
        if num<-2**31:
            return -2**31
        elif num>2**31-1:
            return 2**31-1
        else:
            return num