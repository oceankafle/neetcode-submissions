class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        indexedArr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numFreq[num] = 1 + numFreq.get(num, 0)
        
        for key, val in numFreq.items():
            indexedArr[val].append(key)
        
        final = []
        
        for i in range(len(indexedArr)-1, -1, -1):
            for thing in indexedArr[i]:
                final.append(thing)
                if len(final) == k:
                    return final
        return final
        

                





