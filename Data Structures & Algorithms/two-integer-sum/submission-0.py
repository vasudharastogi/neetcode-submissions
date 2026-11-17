class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsDict = {}

        for i in range(len(nums)):
            summand = target - nums[i]
            if summand in numsDict:
                return [numsDict[summand], i]
            else:
                numsDict[nums[i]] = i
        