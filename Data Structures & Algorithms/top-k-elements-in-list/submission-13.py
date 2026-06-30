class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = [[] for i in range(len(nums) + 1)]
        freq = {}
        #nums = [1, 2, 2, 3, 3, 3, 6, 6, 6]
        final = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for key, value in freq.items():
            mapping[value].append(key)
        
        print(mapping)

        for i in range(len(mapping)-1, -1, -1):
            for item in mapping[i]:
                final.append(item)

                if len(final) == k:
                    return final
        return final





        

        
        
        

