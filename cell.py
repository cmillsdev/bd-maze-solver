from line import Line
from point import Point
from text import Text
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.index = None
        self._win = win
        self.visited = False
        self._center = None

    def __repr__(self):
        return (f"Cell(x1={self._x1}, y1={self._y1}, x2={self._x2}, y2={self._y2}, "
            f"walls={{'left': {self.has_left_wall}, 'right': {self.has_right_wall}, "
            f"'top': {self.has_top_wall}, 'bottom': {self.has_bottom_wall}}}, "
            f"visited={self.visited})")


    def init_geography(self):
        self._tl_corner = Point(self._x1, self._y1)
        self._tr_corner = Point(self._x2, self._y1)
        self._bl_corner = Point(self._x1, self._y2)
        self._br_corner = Point(self._x2, self._y2)
        self._l_line = Line(self._tl_corner, self._bl_corner)
        self._r_line = Line(self._tr_corner, self._br_corner)
        self._t_line = Line(self._tl_corner, self._tr_corner)
        self._b_line = Line(self._bl_corner, self._br_corner)
        self._center = self.get_center()

    def draw(self,x1,y1,x2,y2,i,j):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.index = [i,j]
        if not self._center:
            self.init_geography()
        if self.has_left_wall:
            self._win.draw_line(self._l_line)
        if self.has_right_wall:
            self._win.draw_line(self._r_line)
        if self.has_top_wall:
            self._win.draw_line(self._t_line)
        if self.has_bottom_wall:
            self._win.draw_line(self._b_line)

        # self._win.draw_text(Text(self._center, f"{self.index[0]},{self.index[1]}"))

        if not self.has_left_wall:
            self._win.draw_line(self._l_line, "white")
        if not self.has_right_wall:
            self._win.draw_line(self._r_line, "white")
        if not self.has_top_wall:
            self._win.draw_line(self._t_line, "white")
        if not self.has_bottom_wall:
            self._win.draw_line(self._b_line, "white")

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"

        center = self.get_center()
        other_center = to_cell.get_center()

        move_line = Line(center, other_center)
        self._win.draw_line(move_line, line_color)
    
    def get_center(self):
        center_x = (self._x1 + self._x2)/2
        center_y = (self._y1 + self._y2)/2
        return Point(center_x, center_y)