class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = [] # (pos,speed),time
        pspairs = sorted(zip(position, speed), reverse=True)

        for i in range(len(pspairs)):
            coverdist = target - pspairs[i][0]
            time = coverdist/pspairs[i][1]
            if not stk or time > stk[-1][1]:
                stk.append((pspairs[i],time))        
        return len(stk)