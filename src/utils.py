class Point:
    def __init__(self, x=0, y=0):       
        """Initialize the point with x and y coordinates, defaulting to (0, 0)"""
        self.x = x  # Horizontal coordinate (left to right)
        self.y = y  # Vertical coordinate (top to bottom)

    def __repr__(self):
        """Provide a simple string representation of the Point for debugging purposes"""
        return f"Point(x={self.x}, y={self.y})"
    

class Line:
    def __init__(self, point1, point2):
        """Initialize the line with two points"""
        self.point1 = point1    # Starting point of the line
        self.point2 = point2    # Ending point of the line

    def draw(self, canvas, fill_color='black'):
        """Draw the line on the given canvas with the specified fill color"""
        canvas.create_line(
            self.point1.x, self.point1.y,   # Starting coordinates (x1, y1)
            self.point2.x, self.point2.y,   # Ending coordinates (x2, y2)
            fill=fill_color,                # Color of the line
            width=2                         # Line thickness
        )

    def __repr__(self):
        """Provide a simple string representation of the Line for debugging purposes"""
        return f"Line(Point({self.point1.x}, {self.point1.y}), Point({self.point2.x}, {self.point2.y}))"
    