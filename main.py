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


class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.bg_color = "#C4C4C4"

        self.canvas = tkinter.Canvas(self.root, background=self.bg_color, height=600, width=800)
        self.canvas.pack(anchor="center", expand=1)

        self.rectangle = Rectangle(0, 0, 100, 50, 5, 5)

    def start(self):
        color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
        self.canvas.create_rectangle(self.rectangle.x, self.rectangle.y,
                                     self.rectangle.x + self.rectangle.width, self.rectangle.y + self.rectangle.height,
                                     fill=color, outline=color)
        self.move()
        self.root.mainloop()

    def move(self):
        self.canvas.create_rectangle(self.rectangle.x, self.rectangle.y,
                                     self.rectangle.x + self.rectangle.width, self.rectangle.y + self.rectangle.height,
                                     fill=self.bg_color, outline=self.bg_color)
        self.rectangle.move()
        self.canvas.create_rectangle(self.rectangle.x, self.rectangle.y,
                                     self.rectangle.x + self.rectangle.width, self.rectangle.y + self.rectangle.height,
                                     fill=self.bg_color, outline=self.bg_color)

        color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
        self.canvas.create_rectangle(self.rectangle.x, self.rectangle.y,
                                     self.rectangle.x + self.rectangle.width, self.rectangle.y + self.rectangle.height,
                                     fill=color, outline=color)

        self.root.after(16, self.move)


app = App()
app.start()
