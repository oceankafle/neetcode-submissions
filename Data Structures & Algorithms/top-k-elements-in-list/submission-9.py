class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = [[] for i in range(len(nums) + 1)]
        # nums = [1, 1, 2, 2, 2, 3, 7, 7, 7, 7]
        # 0   1   2   3   4   5       freq
        #[    3   1   2   7    ]      the actual num 

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        final = []
        # {1: 2, 2: 3, 3: 1, 7: 4}
        for key, value in freq.items():
            res[value].append(key)
        
        print(res)
        # [[],[3],[1],[2],[7],[],[],[],[],[],[]]
        for i in range(len(res)-1, 0, -1):  # descending order, starts from end and goes down to index 0
            for n in res[i]:
                final.append(n)

                if len(final) == k:
                    return final
        return final
        # should [7,2]


        
        
                

                


