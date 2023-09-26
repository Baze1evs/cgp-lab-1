import math
import random
import tkinter


def vector_length(vec):
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2)


class Rectangle:
    def __init__(self, x, y, width, height, v_x, v_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.v_x = v_x
        self.v_y = v_y
        self.mass = width * height

    def move(self, rectangles):
        # Обновление координат прямоугольника
        old_x = self.x
        old_y = self.y
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y

        # Проверка столкновения с границами поля
        if self.x < 0 or self.x + self.width > 400:
            self.v_x *= -1  # Изменение направления по x
        if self.y < 0 or self.y + self.height > 300:
            self.v_y *= -1  # Изменение направления по y

        # Проверка столкновения с другими прямоугольниками
        for other_rect in rectangles:
            if self is not other_rect:  # Исключаем текущий прямоугольник из проверки
                if self.intersects(other_rect):
                    # Вычисление вектора между центрами столкновения
                    collision_vector = (other_rect.x - (2*self.x + self.width) / 2,
                                        other_rect.y - (2*self.y + self.height) / 2)
                    # Нормализация вектора
                    length = math.sqrt(collision_vector[0]**2 + collision_vector[1]**2)
                    collision_vector = (collision_vector[0] / length, collision_vector[1] / length)
                    # Вычисление нового вектора скорости после столкновения
                    dot_product = self.v_x * collision_vector[0] + self.v_y * collision_vector[1]
                    self.v_x -= 2 * dot_product * collision_vector[0]
                    self.v_y -= 2 * dot_product * collision_vector[1]

        # Проверка столкновения с другими прямоугольниками после обновления
        for other_rect in rectangles:
            if self is not other_rect:  # Исключаем текущий прямоугольник из проверки
                if self.intersects(other_rect):
                    # Вернуть прямоугольнику старые координаты
                    self.x = old_x
                    self.y = old_y

    def intersects(self, other):
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)

    def out_of_bound(self):
        x, y = 0, 0

        if self.x < 0:
            x = self.x
        elif self.x + self.width > 400:
            x = self.x + self.width - 400

        if self.y < 0:
            y = self.y
        elif self.y + self.height > 300:
            y = self.y + self.height - 300

        return x, y


class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.bg_color = "#C4C4C4"

        self.canvas = tkinter.Canvas(self.root, background=self.bg_color, height=300, width=400)
        self.canvas.pack(anchor="center", expand=1)

        self.rectangles = []

    def add_rectangle(self, x, y, width, height, v_x, v_y):
        self.rectangles.append(Rectangle(x, y, width, height, v_x, v_y))

    def draw_rectangle(self, rectangle, color):
        self.canvas.create_rectangle(rectangle.x, rectangle.y,
                                     rectangle.x + rectangle.width, rectangle.y + rectangle.height,
                                     fill=color, outline=color, tags='rectangles')

    def start(self):
        for rectangle in self.rectangles:
            color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
            self.draw_rectangle(rectangle, color)
        self.update()
        self.root.mainloop()

    def update(self):
        self.canvas.delete('rectangles')
        for rectangle in self.rectangles:
            self.draw_rectangle(rectangle, self.bg_color)
            rectangle.move(self.rectangles)
            self.draw_rectangle(rectangle, self.bg_color)

            color = random.choice(['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta'])
            self.draw_rectangle(rectangle, color)

        self.root.after(10, self.update)


app = App()
app.add_rectangle(0, 0, 50, 25, 2, 3)
app.add_rectangle(300, 0, 50, 25, -2, 2)
app.add_rectangle(200, 200, 50, 50, -10, -10)
app.start()
