#Given a sorted array and a target value, return the index if the target is found.
#Input: [1,3,5,6], Target:7 Output: 4
#Input: [1,3,5,6], Target:5 Output: 2
#Input: [1,3,5,6], Target:2 Output: 1
#Input: [1,3,5,6], Target:0 Output: 0
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([x for x in nums if x < target])
            
