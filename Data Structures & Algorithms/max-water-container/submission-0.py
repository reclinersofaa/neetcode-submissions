class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i in range(len(heights)):
            for j in range(i,len(heights)):
                print(i,j, "gives")
                width = j - i
                area = min(heights[i],heights[j])*width
                print(width, area)
                if area > maxArea:
                    maxArea = area

        return maxArea