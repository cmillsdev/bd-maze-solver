from line import Line
from point import Point
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
        self._win = win
        self.visited = False

    def __repr__(self):
        return f"{self._x1},{self._y1},{self._x2},{self._y2}"

    def init_geography(self):
        self._tl_corner = Point(self._x1, self._y1)
        self._tr_corner = Point(self._x1, self._y2)
        self._bl_corner = Point(self._x2, self._y1)
        self._br_corner = Point(self._x2, self._y2)
        self._l_line = Line(self._tl_corner, self._bl_corner)
        self._r_line = Line(self._tr_corner, self._br_corner)
        self._t_line = Line(self._tl_corner, self._tr_corner)
        self._b_line = Line(self._bl_corner, self._br_corner)
        self._center = self.get_center()

    def draw(self,x1,y1,x2,y2):
        if self._win == None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.init_geography()
        if self.has_left_wall:
            self._win.draw_line(self._l_line)
        if self.has_right_wall:
            self._win.draw_line(self._r_line)
        if self.has_top_wall:
            self._win.draw_line(self._t_line)
        if self.has_bottom_wall:
            self._win.draw_line(self._b_line)

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

        center = self._center
        other_center = to_cell._center
        # left
        if center.x > other_center.x and center.y == other_center.y: 
            wall_center = self._l_line.get_center()
        # right
        elif center.x < other_center.x and center.y == other_center.y: 
            wall_center = self._r_line.get_center()
        # top
        elif center.y < other_center.y and center.x == other_center.x: 
            wall_center = self._t_line.get_center()
        # bottom
        elif center.y > other_center.y and center.x == other_center.x: 
            wall_center = self._b_line.get_center()

        move_line = Line(center, wall_center)
        move_line_to = Line(wall_center, other_center)
        self._win.draw_line(move_line)
        self._win.draw_line(move_line_to)
    
    def get_center(self):
        center_x = (self._x1 + self._x2)/2
        center_y = (self._y1 + self._y2)/2
        return Point(center_x, center_y)