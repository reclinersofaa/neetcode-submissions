class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        m1, m2, m3 = 0, 0, 0

        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            m1 = max(m1, i[0])
            m2 = max(m2, i[1])
            m3 = max(m3, i[2])
            print(m1, m2, m3)

        return [m1, m2, m3] == target