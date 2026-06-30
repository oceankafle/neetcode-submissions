class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1] # copies of left and right halves 
            i, j, k = L, 0, 0 # zeros b/c they start at 0 for left and right halves
            while j < len(left) and k < len(right): # while they're still in bounds
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if  l == r: # size of arr is 1
                return
            m = (l + r) // 2
            mergeSort(arr, l, m) # run on left half
            mergeSort(arr, m + 1, r) # run on right half
            merge(arr, l, m, r)
            return

        mergeSort(nums, 0, len(nums) - 1)
        return nums




