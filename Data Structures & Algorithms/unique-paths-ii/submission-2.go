func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    m, n := len(obstacleGrid), len(obstacleGrid[0])
    memo := make([][]int, m + 1)
    for i := range m + 1 {
        memo[i] = make([]int, n + 1)
    }
    
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            if obstacleGrid[i][j] == 1 {
                memo[i][j] = 0
            } else if i == m -1 && j == n - 1 {
                memo[i][j] = 1
            } else {
                memo[i][j] = memo[i][j + 1] + memo[i+1][j]
            }
        }
    }

    return memo[0][0]
}