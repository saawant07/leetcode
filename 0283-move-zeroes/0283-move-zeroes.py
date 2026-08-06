class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        front=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[front]=nums[i]
                front+=1
        
        while front<len(nums):
            nums[front]=0
            front+=1
        return nums

        return nums 