#Given a 32-bit signed integer, reverse digits of an integer.
#Input: 123 , Output: 321
#Input: 120 , Output: 21
#Input: -123 ,Output: -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        integer = int(str(abs(x))[::-1])
        if integer > 2**31-1 or integer < -2**31-1 or integer ==0:
            return 0
        if x > 0:
            return integer
        if x < 0:
            return -integer
