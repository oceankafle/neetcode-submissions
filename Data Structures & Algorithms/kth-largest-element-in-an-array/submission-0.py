class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # thought process
        # turn this into a maxHeap
        # if numofPops = k, then we're done and return that elem
        # if we pop but numPops != k, then we keep popping and incrementing until it hits k.
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap) # [-4, -3 ,-2, -1, -1], k = 3
        numPops = 0

        while numPops != k:
            value = -heapq.heappop(maxHeap)
            numPops += 1

            if numPops == k:
                return value
        # when they are equal 

        # value = 5, numPops = 1
        # value = 5, numPops = 2
        # value = 4, numPops = 3

