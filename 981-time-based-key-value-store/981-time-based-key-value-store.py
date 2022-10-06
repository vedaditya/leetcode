from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        stack=self.dic[key]
        i=len(stack)-1
        while  stack[i][0]>timestamp and i>=0:
            i-=1
        if i==-1:
            return ""
        return stack[i][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)