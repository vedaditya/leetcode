class StockPrice:

    def __init__(self):
        self.price=dict()
        self.maxx=0
        self.maxh=[]
        self.minh=[]

    def update(self, timestamp: int, price: int) -> None:
        self.price[timestamp]=price
        self.maxx=max(self.maxx,timestamp)
        
        heappush(self.maxh,(-price,timestamp))
        heappush(self.minh,(price,timestamp))

    def current(self) -> int:
        return self.price[self.maxx]

    def maximum(self) -> int:
        price,time=heappop(self.maxh)
        while -price!=self.price[time]:
            price,time=heappop(self.maxh)
        heappush(self.maxh,(price,time))
        return -price

    def minimum(self) -> int:
        price,time=heappop(self.minh)
        while price!=self.price[time]:
            price,time=heappop(self.minh)
        heappush(self.minh,(price,time))
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()