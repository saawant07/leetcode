class Solution(object):
    def singleNumber(self, nums):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key in count:
            if count[key] == 1:
                return key