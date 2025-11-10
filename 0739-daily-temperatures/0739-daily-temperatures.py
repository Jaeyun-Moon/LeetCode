class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] 

        for ind,t in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                result[prev] = ind - prev
            
            stack.append(ind)
        return result