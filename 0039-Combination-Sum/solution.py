class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list1=[]
        def backtracing(start,target,path,total):
            if target==total:
                list1.append(path[:])
                return
            if target<total:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtracing(i,target,path,total+candidates[i])
                path.pop()
        backtracing(0,target,[],0)
        return list1
