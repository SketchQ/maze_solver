from gui import Window
from utils import Point, Line

def main():
    # Create a window with 800x600 pixels
    win = Window(800, 600)

    # Create points
    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(100, 300)
    p4 = Point(300, 300)

    # Create lines between points
    line1 = Line(p1, p2)
    line2 = Line(p2, p4)
    line3 = Line(p4, p3)
    line4 = Line(p3, p1)

    # Draw lines on the window
    win.draw_line(line1, fill_color="red")
    win.draw_line(line2, fill_color="green")
    win.draw_line(line3, fill_color="blue")
    win.draw_line(line4, fill_color="yellow")

    # Wait for the window close
    win.wait_for_close()    

if __name__ == "__main__":
    main()
