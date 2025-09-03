from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if nums[i] in di:
                return [i, di[nums[i]]]
            else:
                di[temp] = i
        return 0