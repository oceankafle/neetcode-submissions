class KthLargest:
    import heapq
    # to turn something into a heap = O(n) but popping every time so O(nlogn) to match size of k
    # min heap of size k, always return arr[0]
    # add/pop = log(n) time

    def __init__(self, k: int, nums: List[int]): # O(n*log(n)), 
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # use python built in function

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)



    def add(self, val: int) -> int: # log(n) time and then m times so m*log(n)
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


        
