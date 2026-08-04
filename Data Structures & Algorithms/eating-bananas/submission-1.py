class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minr = float('inf')

        while l <= r:
            mean = (l + r)//2
            tottime = 0
            for pile in piles:
                tottime += math.ceil(pile/mean)

            if tottime > h:
                l = mean + 1
            elif tottime <= h:
                minr = min(minr, mean) 
                r = mean - 1
        
        return minr
            
        
            
