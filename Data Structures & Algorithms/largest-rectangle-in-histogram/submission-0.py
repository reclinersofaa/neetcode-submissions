class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stk = [] #val,index

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                index, height = stk.pop()
                maxA = max(maxA, height * (i - index))
                start = index
            stk.append([start, h])

        print(stk)
        for i, h in stk:
            maxA = max(maxA, h * (len(heights) - i))
        
        return maxA