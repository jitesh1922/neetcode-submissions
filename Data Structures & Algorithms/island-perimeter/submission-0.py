class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        print(row, col)
        result  = 0
        cor = [[-1,0], [0,-1], [1, 0], [0,1]]
        for i in range(row):
            for j in range(col):
                #print(i, j)
                if grid[i][j] == 1:
                    for dx, dy in cor:
                        #print(dx, dy)
                        x = i + dx
                        y = j + dy
                        if x < 0 or x >= row or y < 0 or y >= col:
                            result += 1
                        elif grid[x][y] == 0:
                            result += 1
        

        return result