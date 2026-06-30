class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use (x1-x2)^2 + (y1-y2)^2
        # points = [[0, 2], [2, 2]]
        final = []
        minHeap = []
        for x,y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while k > 0 and minHeap:
            dist, x, y = heapq.heappop(minHeap)
            final.append([x, y])
            k -= 1
        return final




