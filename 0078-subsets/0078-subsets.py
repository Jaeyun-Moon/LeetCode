class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def dfs(index,prev):
            res.append(prev)
            
            for ind in range(index,len(nums)):
                dfs(ind+1,prev+[nums[ind]]) # ind 대신 index를 사용하였음 (실수)

        dfs(0,[])
        return res
