import pygame
from colors import Colors

class Board:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_colors()

    # COLLISION CHECKS
    def is_inside(self, row: int, col: int) -> bool:
        if (row >= 0) and (row < self.num_rows) and (col >= 0) and (col < self.num_cols):
            return True
        return False

    def is_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] not in [1, 2, 3, 4, 5, 6, 7]
    
    # CLEAR ROWS
    def is_row_full(self, row: int) -> bool:
        for col in range(self.num_cols):
            if not self.grid[row][col]:
                return False
        return True

    def clear_row(self, row) -> None:
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    
    def move_row_down(self, row: int, rows_cleared: int) -> None:
        for col in range(self.num_cols):
            self.grid[row + rows_cleared][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_rows(self) -> None:
        cleared = 0
        for row in range(self.num_rows - 1, 0, - 1):
            if self.is_row_full(row):
                self.clear_row(row)
                cleared += 1
            elif cleared >= 1:
                self.move_row_down(row, cleared)
    
    # DRAW CELLS
    def draw(self, screen: pygame.display) -> None:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)

                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)