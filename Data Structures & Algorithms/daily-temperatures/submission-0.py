class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk = [] #(temp, index)

        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                stkt, stki = stk.pop()
                res[stki] = i - stki 
            stk.append((temperatures[i],i))
        
        return res

