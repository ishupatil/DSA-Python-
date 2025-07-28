class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        prev={}
        for i in range(0,n):
            diff = target-nums[i]
            if diff in prev:
                return [prev[diff],i]
            prev[nums[i]]=i
        