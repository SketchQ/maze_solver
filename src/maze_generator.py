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
        