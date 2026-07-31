class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=len(nums)
        for j in range(i):
            for k in range(j+1,i):
                if (nums[j]+nums[k])==target:
                    return [j,k]
        