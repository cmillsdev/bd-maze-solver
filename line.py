from point import Point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y,fill=fill_color,width=2)

    def get_center(self):
        center_x = (self.p1.x + self.p2.x)/2
        center_y = (self.p1.y + self.p2.y)/2
        return Point(center_x, center_y)