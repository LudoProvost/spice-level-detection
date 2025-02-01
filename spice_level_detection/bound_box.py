class BoundBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return f"BoundBox(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"