class Solution:
    def maximalSquare(self, matrix) -> int:
        if len(matrix) == 0:
            return 0
        W, H = len(matrix), len(matrix[0])
        d = {}
        found = False
        # Load first level matrix
        for i in range(W):
            for j in range(H):
                d[(i, j, 0)] = int(matrix[i][j])
                if not found and int(matrix[i][j]) == 1:
                    found = True
        if not found:
            return 0

        # Rest of the stuff
        for n in range(1, min(W, H)):
            found = False
            for i in range(0, W - n):
                for j in range(0, H - n):
                    d[(i, j, n)] = \
                        d[(i, j, n-1)] and \
                        d[(i+1, j, n-1)] and \
                        d[(i, j+1, n-1)] and \
                        d[(i+1, j+1, n-1)]
                    if not found and d[(i, j, n)]:
                        found = True
            if not found:
                return n ** 2
        return min(W, H) ** 2


sol = Solution()
arr = [
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"]
]
res = sol.maximalSquare(arr)
print(res)
