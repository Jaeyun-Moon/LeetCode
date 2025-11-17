class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return list(zip(*collections.Counter(nums).most_common(k)))[0]
        count_nums = collections.Counter(nums)
        freqs_heap = [] 

        for c in count_nums:
            heapq.heappush(freqs_heap,(-count_nums[c],c)) 
            # 키 : 빈도 수 의 마이너스, 
            # 파이썬 heapq모듈은 최소 힙(min-heap)만 지원 함
        
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk

