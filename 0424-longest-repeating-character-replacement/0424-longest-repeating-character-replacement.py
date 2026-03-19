class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        count = collections.Counter()

        for right in range(1,len(s)+1):
            count[s[right-1]] += 1 
            max_count_num = count.most_common(1)[0][1] 
        
            if right - left - max_count_num > k:
                count[s[left]] -=1 
                left +=1 
                
        return right-left