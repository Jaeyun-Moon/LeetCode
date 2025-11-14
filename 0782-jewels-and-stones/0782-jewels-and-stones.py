class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # sum(s in J for s in S)
        c = 0 
        splits = collections.Counter(stones)
        for char in jewels:
            c += splits[char]
        return c 