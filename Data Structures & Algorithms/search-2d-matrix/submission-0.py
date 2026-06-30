class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        
        for r in range(rows): # 0, 1, 2
            if matrix[r][-1] == target:
                return True
            elif matrix[r][-1] < target: # means it can't be in this entire row, skip to next row
                # skip to next row
                continue
            elif matrix[r][-1] > target: # we know it's somewhere in this row, perform BS on this arr
                l = 0  # beginning idx of this row
                right = len(matrix[0]) - 1 # end idx of this row

                while l <= right:
                    mid = (l + right) // 2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] < target:
                        l = mid + 1
                    else:
                        right = mid - 1
        return False
                