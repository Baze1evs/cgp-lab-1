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

        dx, dy = self.v_x, self.v_y

        x_out, y_out = self.out_of_bound()
        while (x_out != 0 or y_out != 0) and (dx != 0 or dy != 0):
            # вычисляем обратный шаг и меняем направление на будущее
            if abs(x_out) > abs(y_out):
                y_out = x_out * self.v_y / self.v_x
                self.v_x *= -1
            else:
                x_out = self.v_x * y_out / self.v_y
                self.v_y *= -1

            # шагаем в обратную сторону
            self.x -= x_out
            self.y -= y_out
            dx -= x_out
            dy -= y_out

            self.x += dx
            self.y += dy

            x_out, y_out = self.out_of_bound()

    def intersects(self, other):
        rect1_x = self.x
        rect1_y = self.y
        rect1_right = self.x + self.width
        rect1_bottom = self.y + self.height

        rect2_x = other.x
        rect2_y = other.y
        rect2_right = other.x + other.width
        rect2_bottom = other.y + other.height

        if (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y):
            x_overlap = min(rect1_right, rect2_right) - max(rect1_x, rect2_x)
            y_overlap = min(rect1_bottom, rect2_bottom) - max(rect1_y, rect2_y)

            return x_overlap, y_overlap

        return 0, 0

    def out_of_bound(self):
        x, y = 0, 0

        if self.x < 0:
            x = self.x
        elif self.x + self.width > 800:
            x = self.x + self.width - 800

        if self.y < 0:
            y = self.y
        elif self.y + self.height > 600:
            y = self.y + self.height - 600

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
