import math
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    def minPathSum(self, grid) -> int:
        w = len(grid)
        h = len(grid[0])
        scores = [[None for _ in range(h)] for _ in range(w)]
        q = [(0, 0)]
        while len(q) > 0:
            cur = q.pop(0)
            curX = cur[0]
            curY = cur[1]
            minSur = None
            for d in DIRS:
                x = curX + d[0]
                y = curY + d[1]
                if x >= 0 and x < w and y >= 0 and y < h:
                    if scores[x][y] != None:
                        minSur = scores[x][y] if minSur == None else min(
                            minSur, scores[x][y])
                    else:
                        if (x, y) not in q:
                            q.append((x, y))
            scores[curX][curY] = grid[curX][curY] + \
                (0 if minSur == None else minSur)
        return scores[-1][-1]


sol = Solution()
grid = [
    [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
    [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
    [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
    [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
    [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
    [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
    [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
    [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
    [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
    [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
    [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
    [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]
]
res = sol.minPathSum(grid)
print(res)
