import random
import tkinter


class Rectangle:
    def __init__(self, x, y, width, height, v_x, v_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.v_x = v_x
        self.v_y = v_y
        self.mass = width * height

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def intersects(self, other):
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

    def out_of_bound(self):
        x, y = 0, 0

        if x < 0:
            x = -self.x
        elif x > 800:
            x = 800 - self.x

        if y < 0:
            y = -self.y
        elif y > 600:
            y = 600 - self.y

        return x, y


class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.bg_color = "#C4C4C4"

        self.canvas = tkinter.Canvas(self.root, background=self.bg_color, height=600, width=800)
        self.canvas.pack(anchor="center", expand=1)

        self.rectangles = []

    def add_rectangle(self, x, y, width, height, v_x, v_y):
        self.rectangles.append(Rectangle(x, y, width, height, v_x, v_y))

    def draw_rectangle(self, rectangle, color):
        self.canvas.create_rectangle(rectangle.x, rectangle.y,
                                     rectangle.x + rectangle.width, rectangle.y + rectangle.height,
                                     fill=color, outline=color)

    def start(self):
        for rectangle in self.rectangles:
            color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
            self.draw_rectangle(rectangle, color)
        self.move()
        self.root.mainloop()

    def move(self):
        for rectangle in self.rectangles:
            self.draw_rectangle(rectangle, self.bg_color)
            rectangle.move()
            self.draw_rectangle(rectangle, self.bg_color)

            color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
            self.draw_rectangle(rectangle, color)

        self.root.after(16, self.move)


app = App()
app.add_rectangle(0, 0, 100, 50, 5, 5)
app.add_rectangle(700, 0, 100, 50, -5, 5)
app.start()
