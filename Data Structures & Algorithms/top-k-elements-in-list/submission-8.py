class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # len of array

        # {1: 1, 3: 2, 4: 3}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # count dict = key (count) : value (values from num)
        for key, value in count.items(): # [ [], [1], [3], [4], [], [] ]
            freq[value].append(key)
        
        res = [] # will hold the final values
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res


        
        
                

                


