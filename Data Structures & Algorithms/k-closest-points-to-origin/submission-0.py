class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for i in points:
            dist = (i[0])**2 + (i[1])**2
            dists.append((dist,i))
        
        heapq.heapify(dists)
        print(dists)

        res = []
        for i in range(k):
            res.append(heapq.heappop(dists)[1])
        
        return res
