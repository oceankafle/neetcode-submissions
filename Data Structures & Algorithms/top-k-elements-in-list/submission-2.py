class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}   # dictionary
        freq = [[] for i in range(len(nums) + 1)] # initalize freq size to be length of array

        for n in nums:
            count[n] = 1 + count.get(n, 0) # key 

        for n,c in count.items():
            freq[c].append(n)  # append key from count to the freq arr
        
        res = []
        for i in range(len(freq) -1, 0, -1):  # descending order
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res


        # key value pairs where the key is the frequency : list of numbers
        # run through pass of the array (which is len of nums)

        # Runtime: O(n), one pass of the array



