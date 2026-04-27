func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    memo := make(map[[2]int]int)
    var dfs func(i, j int) int
	dfs = func(i, j int) int {
        if i < 0 || j < 0 || i >= len(obstacleGrid) || j >= len(obstacleGrid[0]) || obstacleGrid[i][j] == 1 {
            return 0
        }
        if i == len(obstacleGrid)-1 && j == len(obstacleGrid[0])-1 {
            return 1
        }
        if val, ok := memo[[2]int{i, j}]; ok {
            return val
        }

        res := dfs(i + 1, j) + dfs(i, j + 1)
        memo[[2]int{i, j}] = res
        return res
    }

    return dfs(0, 0)
}