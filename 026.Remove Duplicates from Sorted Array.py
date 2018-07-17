#Given a sorted array nums, remove the duplicates
#Return the new length.


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        l =len(nums)
        for i in range(l):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
        return last + 1
