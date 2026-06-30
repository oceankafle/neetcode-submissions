class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums = [1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 7, 7, 7]
        freq = {}
        final = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums: # O(n)
            freq[num] = 1 + freq.get(num, 0)
        
        for key, value in freq.items(): # O(n)
            final[value].append(key)
        
        for i in range(len(final)-1, -1, -1):
            for num in final[i]:
                print("I am currently on the number... ", num)
                if len(res) == k:
                    print("I found the values!..", res)
                    return res
                else:
                    print("I am about to add ...", num)
                    res.append(num)
        return res


        
        

# Step 1: create freq dictionary to count freq of numbers in nums
# Step 2: create res arr to store num (value at the index) to the # of times it occurs (index of arr)
# Step 3: loop through the res arr backwards and return the # of elems you need (based off k) 

