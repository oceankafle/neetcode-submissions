class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python doesn't support maxheaps so use minheap with negated vals
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            if first != second:
                heapq.heappush(maxHeap, -(first - second))  # need to push the negative version to the maxHeap

        return -maxHeap[0] if maxHeap else 0
