class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since it's sorted, we can use two pointers to either move left up or right down
        l, r = 0, len(numbers) - 1

        while l <= r:
            addedSum = numbers[l] + numbers[r]

            if addedSum == target:
                return [l + 1, r + 1]
            elif addedSum < target:
                l += 1
            else:
                r -= 1
        return