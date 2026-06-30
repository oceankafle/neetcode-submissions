class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two # update by adding 2 previous values
            two = temp
        return one
