class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for i in points:
            dist = (i[0])**2 + (i[1])**2
            dists.append((-1*dist,i))
            heapq.heapify(dists)
            if len(dists) > k:
                heapq.heappop(dists)

        res = []   
        for i in dists:
            res.append(i[1])
        return res
          