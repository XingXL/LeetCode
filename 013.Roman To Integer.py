# Roman to integer
class Solution:
    def romantointeger(self, s):
        """
        :type s: str
        :rtype: int
        """
        add = 0
        dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        l = len(s)
        for i in range(0, l-1):
            if dict[s[i]] < dict[s[i+1]]:
                add -= dict[s[i]]
            else:
                add += dict[s[i]]
        return add + dict[s[-1]]

        
