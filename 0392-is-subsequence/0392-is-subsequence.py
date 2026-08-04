class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        for i in t:
            if count<len(s) and i==s[count] :
                count+=1
        return count==len(s)