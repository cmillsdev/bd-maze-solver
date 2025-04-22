from time import sleep
import random
from cell import Cell
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._seed = seed
        if seed != None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for x in range(1,self._num_cols+1):
            cell_column = []
            for y in range(1,self._num_rows+1):
                cell_column.append(Cell(self._win))
            self._cells.append(cell_column)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        loops = 0
        while True:
            loops += 1
            to_visit = []
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j, 'l'))
            # right
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j,'r'))
            # top
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1,'t'))
            # bottom
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1,'b'))

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                print(loops)
                return

            i2, j2, d = random.choice(to_visit)
            print(i2, j2, d)

            if d == 'l':
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j2].has_right_wall = False
            if d == 'r':
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j2].has_left_wall = False
            if d == 't':
                self._cells[i][j].has_top_wall = False
                self._cells[i2][j2].has_bottom_wall = False
            if d == 'b':
                self._cells[i][j].has_bottom_wall = False
                self._cells[i2][j2].has_top_wall = False

            self._break_walls_r(i2,j2)

    def _reset_cells_visited(self):
        for c in self._cells:
            for e in c:
                e.visited = False