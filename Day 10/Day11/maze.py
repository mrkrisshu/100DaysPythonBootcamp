import random
from collections import deque

# --- Maze Generation (using a simplified randomized DFS-like approach) ---
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)] # All walls initially
    start_x, start_y = 0, 0
    maze[start_y][start_x] = 0 # Starting point is open

    stack = [(start_x, start_y)]
    visited = set([(start_x, start_y)])

    while stack:
        current_x, current_y = stack[-1]
        neighbors = []

        # Check unvisited neighbors (2 steps away, to carve paths)
        for dx, dy in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            next_x, next_y = random.choice(neighbors)
            # Carve path between current and next
            maze[current_y + (next_y - current_y) // 2][current_x + (next_x - current_x) // 2] = 0
            maze[next_y][next_x] = 0
            visited.add((next_x, next_y))
            stack.append((next_x, next_y))
        else:
            stack.pop()
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(["██" if cell == 1 else "  " for cell in row]))

# --- Common Helper Functions for Maze Solving ---
def get_neighbors(maze, r, c):
    height = len(maze)
    width = len(maze[0])
    neighbors = []
    # Up, Down, Left, Right
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < height and 0 <= nc < width and maze[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def solve_and_print_path(maze, path):
    height = len(maze)
    width = len(maze[0])
    solved_maze = [row[:] for row in maze] # Create a copy

    for r, c in path:
        if (r, c) != path[0] and (r, c) != path[-1]: # Don't mark start/end
            solved_maze[r][c] = '*' # Mark path

    for r in range(height):
        row_str = ""
        for c in range(width):
            if solved_maze[r][c] == 1:
                row_str += "██"
            elif solved_maze[r][c] == '*':
                row_str += "🚶" # Path
            elif (r, c) == path[0]:
                row_str += "🟢" # Start
            elif (r, c) == path[-1]:
                row_str += "🎯" # End
            else:
                row_str += "  " # Empty space
        print(row_str)

# --- DFS (Depth-First Search) Maze Solver ---
def solve_maze_dfs(maze, start, goal):
    stack = []
    stack.append(start)
    came_from = {start: None}
    visited = set([start])

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in get_neighbors(maze, current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
    return None # No path found

# --- BFS (Breadth-First Search) Maze Solver ---
def solve_maze_bfs(maze, start, goal):
    queue = deque()
    queue.append(start)
    came_from = {start: None}
    visited = set([start])

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in get_neighbors(maze, current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
    return None # No path found

# --- Main Execution ---
if __name__ == "__main__":
    maze_width = 21 # Must be odd for this generator
    maze_height = 11 # Must be odd for this generator

    print(f"Generating a {maze_width}x{maze_height} maze...")
    my_maze = generate_maze(maze_width, maze_height)

    start_point = (0, 0)
    end_point = (maze_height - 1, maze_width - 1)

    print("\n--- Original Maze ---")
    print_maze(my_maze)

    # --- DFS Solver ---
    print("\n--- Solving with DFS ---")
    dfs_path = solve_maze_dfs(my_maze, start_point, end_point)
    if dfs_path:
        print("Path found (DFS):")
        solve_and_print_path(my_maze, dfs_path)
        print(f"Path length (DFS): {len(dfs_path)}")
    else:
        print("No path found using DFS.")

    # --- BFS Solver ---
    print("\n--- Solving with BFS ---")
    bfs_path = solve_maze_bfs(my_maze, start_point, end_point)
    if bfs_path:
        print("Path found (BFS):")
        solve_and_print_path(my_maze, bfs_path)
        print(f"Path length (BFS): {len(bfs_path)}")
    else:
        print("No path found using BFS.")