DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def numIslands(self, grid) -> int:
        check = [[False for _ in x] for x in grid]
        w = len(grid)
        if w == 0:
            return 0
        h = len(grid[0])
        islands = 0
        for i in range(w):
            for j in range(h):
                if check[i][j] == False:
                    check[i][j] = True
                    if grid[i][j] == "1":
                        islands += 1
                    q = [(i, j)]
                    isl = grid[i][j]
                    while len(q) > 0:
                        cur = q.pop(0)
                        for d in DIRS:
                            x = cur[0] + d[0]
                            y = cur[1] + d[1]
                            if x >= 0 and x < w and y >= 0 and y < h and \
                                    not check[x][y] and grid[x][y] == isl:
                                q.append((x, y))
                                check[x][y] = True
        return islands


sol = Solution()
grid = [
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
print(sol.numIslands(grid))
