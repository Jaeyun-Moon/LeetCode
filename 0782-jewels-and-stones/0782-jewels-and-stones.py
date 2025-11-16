class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        char_count = collections.Counter(stones)
        nums = 0
        for c in jewels:
            nums += char_count[c]
        return nums 