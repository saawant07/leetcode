class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for i in operations:
            if i =="+":
                if len(result)>=2:
                    result.append(result[-1] + result[-2])
            elif i == "D":
                if result:
                    result.append(result[-1]*2)
            elif i =="C":
                if result:
                    result.pop()
            else:
                result.append(int(i))

        return sum(result)

