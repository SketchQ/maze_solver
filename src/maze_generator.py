import tkinter as tk

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        """
        Initialize the cell with its boundaries and canvas window.

        :param x1 : Top-left x coordinate
        :param y1 : Top-left y coordinate
        :param x2 : Bottom-right x coordinate
        :param y2 : Bottom-right y coordinate
        :param win: Canvas or window where the cell is drawn
        """

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        '''
        Draw the cell on the canvas by checking which walls it has.
        '''
        # Draw left wall
        if self.has_left_wall:
            self._win.create_line(self._x1, self._y1, self._x1, self._y2)
        # Draw the top wall
        if self.has_top_wall:
            self._win.create_line(self._x1, self._y1, self._x2, self._y1)
        # Draw the right wall
        if self.has_right_wall:
            self._win.create_line(self._x2, self._y1, self._x2, self._y2)
        # Draw the bottom wall
        if self.has_bottom_wall:
            self._win.create_line(self._x1, self._y2, self._x2, self._y2)
    
    def draw_move(self, to_cell, undo=False):
        '''
        Draw a line connecting the center of this cell to the center of another cell.

        :param to_cell: The target cell to draw the move to.
        :param undo: If True, the line is drawn in gray to represent backtracking.
        '''
        # Calculate the center of the current cell
        center_x1 = (self._x1 + self._x2) / 2
        center_y1 = (self._y1 + self._y2) / 2

        # Calculate the center of the target cell
        center_x2 = (to_cell._x1 + to_cell._x2) / 2
        center_y2 = (to_cell._y1 + to_cell._y2) / 2

        # Set the color based on the undo flag
        color = "gray" if undo else "red"

        # Draw the line between the two centers
        self._win.create_line(center_x1, center_y1, center_x2, center_y2, fill=color, width=2)