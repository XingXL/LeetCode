#Input:candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#] 



class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.combine_sum2(candidates, 0, [], result, target)
        return result
    
    def combine_sum2(self, nums, start, path, result, target):
        if not target:
            return result.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.combine_sum2(nums, i + 1, path + [nums[i]],result, target - nums[i])
