class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted 2 sum --> using 2 pointers this time to get sum then compare it with target, move 

        l, r = 0, len(numbers) - 1

        while l < r:
            sumOf2 = numbers[l] + numbers[r]

            if sumOf2 == target:
                return [l+1, r+1]
            elif sumOf2 < target:
                l += 1
            else:
                r -= 1
        return []
            