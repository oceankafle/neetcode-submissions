class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # Step 1: create freq dictionary to count freq of numbers in nums
        # Step 2: create res arr to store num (value at the index) to the # of times it occurs (index of arr)
        # Step 3: loop through the res arr backwards and return the # of elems you need (based off k) 
        freq = {}
        res = [[] for i in range(len(nums) + 1)]
        final = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        print(freq)
        for key, value in freq.items():
            res[value].append(key)
        print(res)

        for i in range(len(res)-1, -1, -1):
            for num in res[i]:
                final.append(num)

                if len(final) == k:
                    return final
        return final


        
        
                

                


