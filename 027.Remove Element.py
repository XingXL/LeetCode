#Remove Element
#Given nums = [3,2,2,3], val = 3, remove all instances same with the val.
#Your function should return lenth = 2, with the first two elements of nums being 2.
#It doesn't matter what you leave beyond the returned length.

Class Solution:
    def removeElement(self, nums, val):
                """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        last = len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1
