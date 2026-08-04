class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #initialize heap with count
        heap = []
        for cnt in count.values():
            heap.append(-1*cnt)
        heapq.heapify(heap)

        time = 0 #initialize time and queue
        q = deque()

        while heap or q: 
            time += 1
            if heap: #check heap, pop, add value into queue if non-zero
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c,time + n])
            
            if q and q[0][1] == time: #add queue ele to heap if time reached
                heapq.heappush(heap, q.popleft()[0])
            
        return time