#Input: haystack = "hello", needle = "ll",Output: 2
#Input: haystack = "aaaaa", needle = "bba", Output: -1

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
