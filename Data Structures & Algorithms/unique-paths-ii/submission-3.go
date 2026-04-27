func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    m, n := len(obstacleGrid), len(obstacleGrid[0])
    memo := make([]int, n + 1)
    
    if obstacleGrid[0][0] == 1 {
        return 0
    }
    memo[1] = 1
    for i := 1; i <= m; i++{
        new_memo := make([]int, n + 1)
        for j := 1; j <= n; j++ {
            if obstacleGrid[i-1][j-1] == 1 {
                new_memo[j] = 0
            } else {
                new_memo[j] = new_memo[j - 1] + memo[j]
            }
        }

        memo = new_memo
    }


    return memo[n]
}