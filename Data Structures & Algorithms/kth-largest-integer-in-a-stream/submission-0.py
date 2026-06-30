class KthLargest:
    import heapq
# implement a max heap 

    def __init__(self, k: int, nums: List[int]):
       self.minHeap = nums
       self.k = k
       heapq.heapify(self.minHeap) # heapify the list
       while len(self.minHeap) > k: # we need to pop elements until its size of k
        heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # add the val to the heap
        if len(self.minHeap) > self.k: # if size of heap > k
            heapq.heappop(self.minHeap) # pop until its same size
        return self.minHeap[0] # we know the min elem is the kth largest




# idea behind this is we always take the min element from our min 
# heap because we will always make sure the size of the minheap is 
# equal to k.

        
