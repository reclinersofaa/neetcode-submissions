class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
            print(count)

        arr = []
        for num, c in count.items():
            arr.append([c,num])
            print(arr)
        arr.sort()
        print(arr)

        res = []
        while (len(res)<k):
            res.append(arr.pop()[1])
            print(res)
        
        return res
        
