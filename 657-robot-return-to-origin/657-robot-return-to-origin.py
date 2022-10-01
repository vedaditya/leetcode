class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos=[0,0]
        dirr={"R":[1,0],"U":[0,1],"L":[-1,0],"D":[0,-1]}
        for i in moves:
            pos[0]+=dirr[i][0]
            pos[1]+=dirr[i][1]
        return True if pos==[0,0] else False 