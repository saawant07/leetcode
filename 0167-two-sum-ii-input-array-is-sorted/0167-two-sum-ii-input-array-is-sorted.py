class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=0
        high=len(nums)-1
        for i in range(len(nums)):
            sum=nums[low]+nums[high]
            if sum<target:
                low+=1
            elif target<sum:
                high-=1
        a=[low+1,high+1]
        return a