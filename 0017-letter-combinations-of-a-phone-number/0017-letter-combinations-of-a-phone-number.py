class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = [] 
        dig = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def dfs(index,combi):
            if len(combi) == len(digits):
                result.append(combi)
                return 
            
            for i in range(index,len(digits)):
                for j in  dig[digits[i]]:
                    dfs(i+1,combi+j)

        if not digits:
            return [] 

        dfs(0,'')
        
        return result
