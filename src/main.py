from gui import Window
from utils import Point, Line
from maze_generator import Cell

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

    # Add Cell class testing
    # Create cells
    cell1 = Cell(400, 100, 500, 200, win.canvas)  # A cell at (400, 100) to (500, 200)
    cell1.has_left_wall = False  # Remove the left wall
    cell1.draw()  # Draw the first cell

    cell2 = Cell(520, 100, 620, 200, win.canvas)  # A cell adjacent to the first
    cell2.has_top_wall = False  # Remove the top wall
    cell2.draw()  # Draw the second cell

    cell3 = Cell(400, 220, 500, 320, win.canvas)  # A cell below the first
    cell3.has_right_wall = False  # Remove the right wall
    cell3.draw()  # Draw the third cell

    cell4 = Cell(520, 220, 620, 320, win.canvas)  # A diagonal cell
    cell4.has_bottom_wall = False  # Remove the bottom wall
    cell4.draw()  # Draw the fourth cell

    # Draw a forward move between the two cells
    cell1.draw_move(cell2, undo=False)

    # Simulate backtracking
    cell2.draw_move(cell1, undo=True)

    # Wait for the window close
    win.wait_for_close()    

if __name__ == "__main__":
    main()
