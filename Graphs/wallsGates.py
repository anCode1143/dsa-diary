class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        dist = 1
        while queue:
            level = len(queue)
            for _ in range(level):
                row, col = queue.popleft()
                steps = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                for step in steps:
                    if 0 <= step[0] < ROWS and 0 <= step[1] < COLS and rooms[step[0]][step[1]] == 2147483647:
                        rooms[step[0]][step[1]] = dist
                        queue.append(step)
            dist += 1