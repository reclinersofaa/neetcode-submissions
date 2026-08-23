class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        cmap = Counter(hand)

        minH = list(cmap.keys()) #use minheap to immediately find the min val in usable elements in count
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            
            if cmap[first] == 0:
                heapq.heappop(minH)
                continue #pop that from queue and dont go with it later
            
            for i in range(first, first + groupSize):
                if i not in cmap or not cmap[i]:
                    return False
                cmap[i] -= 1
            
        return True