class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        # small = maxHeap since we want the biggest from the smalls [1, 2, 3]
        # large = minHeap since we want the smallest from the bigs  [4, 5, 6]
        # pop from each to compute median if the heaps are equal in size

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) # maxheaps are minheaps with negated values

        # if max from small heap is somehow > than the min from large heap:
        if (self.small and self.large and -(self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small) # negate to turn it positive
            heapq.heappush(self.large, val)
        
        # if size of small heap bigger than large heap --> we are able to push it because everything is in sorted order already
        if len(self.small) > len(self.large) + 1:
           val = -heapq.heappop(self.small)
           heapq.heappush(self.large, val)
        
        # size of large bigger than small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large): # we know one of them has odd # of elements
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        # they're equal in size
        return (-self.small[0] + self.large[0]) / 2

        





