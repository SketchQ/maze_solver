from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Create a root widget for the main window
        self.root = Tk()

        # Set the title of the window
        self.root.title("Maze Solver Window")

        # Create a Canvas widget with the given width and height
        self.canvas = Canvas(self.root, width=width, height=height)

        # Pack the canvas widget so it's ready for drawing
        self.canvas.pack(fill=BOTH, expand=True)

        # Running flag to indicate wheter the window is active
        self.running = False

        # Set up the protocol to trigger the close method on window close
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """
        Redraws all the graphics in the window by calling Tkinter's update methods.
        """
        self.root.update_idletasks()    # Handles pending tasks like resizing
        self.root.update()              # Redraws the window and all its content

    def wait_for_close(self):
        """
        Keeps the window running and continuosly redraws the window
        until the window is closed or the running state is changed to False.
        """

        # Set the running flag to True to indicate the window is active
        self.running = True

        # Keep redrawing the window while the running state is True
        while self.running:
            self.redraw()   # Redraw the window and its content repeatedly

    def close(self):
        """
        Stops the window loop and closes the application
        """

        self.running = False    # Set the running flag to False to exit the loop
        self.root.destroy()     # Destroy the Tkinter window and exit the program