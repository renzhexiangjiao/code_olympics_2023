def co_headcount(grid):

    rows = len(grid)
    cols = len(grid[0])

    count = []
    index = -1

    # DFS search of grid
    def dfs(row, col):
        # check for edges
        if row < 0 or row == rows or col < 0 or col == cols:
            return

        # check if no longer at teams table
        if grid[row][col] != 1:
            return

        # set person a visited
        grid[row][col] = "V"

        # add person to count of team
        count[index] += 1

        # recursively check beside player
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count.append(0)
                index += 1
                dfs(r, c)

    if len(count) == 0:
        return "0 teams"
    if len(count) == 1:
        return f"1 team of {count} totalling {count[0]}"

    return f"{len(count)} teams of {sorted(count, reverse= True)} totalling {sum(count)}"
