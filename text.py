class Text:
    def __init__(self, p, text):
        self.p = p
        self.text = text.strip()

    def draw(self, canvas):
        canvas.create_text((self.p.x,self.p.y),text=self.text,fill="black",width=0, justify="center")