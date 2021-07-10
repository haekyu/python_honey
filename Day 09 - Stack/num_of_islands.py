class Stack:

    def __init__(self):
        self.store = []

    def is_empty(self):
        return len(self.store) == 0

    def push(self, e):
        self.store.append(e)

    def pop(self):
        if len(self.store) == 0:
            return None
        last = self.store[-1]
        self.store = self.store[:-1]
        return last


def parse_island(file_path):

    # Read island data
    f = open(file_path)
    M = f.readlines()
    f.close()

    # Parse island data
    for row, row_val in enumerate(M):
        M[row] = [int(char) for char in row_val.replace('\n', '')]
    
    return M


def pick_direction(curr, M, visited):

    move_delta = [
        [-1, 0], # up
        [1, 0], # down
        [0, -1], # left
        [0, 1] # right
    ]

    curr_row = curr[0]
    curr_col = curr[1]
    max_row = len(M) - 1
    max_col = len(M[0]) - 1

    for move in move_delta:

        next_row = curr_row + move[0]
        next_col = curr_col + move[1]

        if (next_row < 0) or (next_row > max_row):
            continue

        if (next_col < 0) or (next_col > max_col):
            continue

        if M[next_row][next_col] == 0:
            continue

        if (next_row, next_col) in visited:
            if visited[(next_row, next_col)]:
                continue

        return move

    return None


def dfs(start_row, start_col, M, visited):
    """
    In M,
        1 - land
        0 - water
    Starting from the (start_row, start_col), 
    traverse M by the dfs approach and
    mark visited grids in `visited`.
    Return the updated `visited`
    """

    stack = Stack()
    stack.push((start_row, start_col))

    while not stack.is_empty():

        # Current point
        curr = stack.pop()
        visited[curr] = True

        # Pick direction to move from curr
        move = pick_direction(curr, M, visited)
        if move is None:
            continue

        # Go to the next move
        next_row = curr[0] + move[0]
        next_col = curr[1] + move[1]
        stack.push((next_row, next_col))

    return visited


def count_num_islands(M):

    num = 0
    num_row = len(M)
    num_col = len(M[0])
    visited = {}

    for row in range(num_row):
        for col in range(num_col):

            # Skip, if current point is a water
            if M[row][col] == 0:
                continue

            # Skip, if current point is a land but visited
            if (row, col) in visited:
                if visited[(row, col)]:
                    continue

            # If current point is a land and not visited
            num = num + 1
            visited = dfs(row, col, M, visited)

    return num


if __name__ == '__main__':
    M = parse_island('./island.txt')
    num = count_num_islands(M)
    print(num)

