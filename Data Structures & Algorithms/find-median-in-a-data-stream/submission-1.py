import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            ele = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, ele)
        
        if len(self.small) > len(self.large) + 1: 
            ele = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, ele)

        if len(self.large) > len(self.small) + 1:
            ele = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * ele)           

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1*self.small[0] + self.large[0])/2

        