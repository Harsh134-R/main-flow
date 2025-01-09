import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)]  # 1 for walls, 0 for paths
        self.solution = None

    def generate_maze(self):
        def dfs(x, y):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                if 0 < nx < self.rows and 0 < ny < self.cols and self.grid[nx][ny] == 1:
                    self.grid[x + dx][y + dy] = 0
                    self.grid[nx][ny] = 0
                    dfs(nx, ny)

        self.grid[1][1] = 0
        dfs(1, 1)

    def solve_maze(self):
        def dfs(x, y, path):
            if (x, y) == (self.rows - 2, self.cols - 2):
                self.solution = path[:]
                return True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0 and (nx, ny) not in path:
                    path.append((nx, ny))
                    if dfs(nx, ny, path):
                        return True
                    path.pop()
            return False

        self.solution = None
        dfs(1, 1, [(1, 1)])

    def display_maze(self):
        for row in self.grid:
            print("".join("█" if cell == 1 else " " for cell in row))

    def display_solution(self):
        if not self.solution:
            print("No solution found.")
            return
        solution_set = set(self.solution)
        for x in range(self.rows):
            for y in range(self.cols):
                if (x, y) in solution_set:
                    print(".", end="")
                else:
                    print("█" if self.grid[x][y] == 1 else " ", end="")
            print()

if __name__ == "__main__":
    rows, cols = 21, 21  # Maze dimensions 
    maze = Maze(rows, cols)

    print("Generating maze...")
    maze.generate_maze()
    maze.display_maze()

    print("\nSolving maze...")
    maze.solve_maze()
    maze.display_solution()
