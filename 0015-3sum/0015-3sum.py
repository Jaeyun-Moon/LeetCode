class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [] 

        for i in range(len(nums)-1):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val < 0:
                    left +=1 
                    while left<right and nums[left-1] == nums[left]:
                        left+=1 
                elif val > 0:
                    right-=1
                    while left < right and nums[right+1] == nums[right-1]:
                        right -=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1 
                    right-=1 
                    while left<right and nums[left-1] == nums[left]:
                        left+=1 
                    while left < right and nums[right+1] == nums[right-1]:
                        right -=1
        return result
                

        