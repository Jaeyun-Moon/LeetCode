class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = collections.deque()
        l = 0
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        #print(q)
        l = 0
        for r in range(k, len(nums)):
         #   print(q)
            if q and q[0] == nums[l]:
                q.popleft()
            l += 1
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            res.append(q[0])
        #print(res)
        return res
