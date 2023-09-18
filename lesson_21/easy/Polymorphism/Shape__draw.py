# Створіть клас Shape з методом draw().
# Створіть підкласи Circle, Rectangle, та Triangle, які успадковують Shape та реалізовують
# свої методи draw(). Створіть список різних фігур та викличте метод draw() для кожної з них.
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Shape:
    def draw(self):
        raise NotImplementedError("Метод draw() повинен бути реалiзованим у пiдкласах!")


class Circle(Shape):
    def draw(self):
        fig, ax = plt.subplots()
        ax.add_patch(patches.Circle((0.5, 0.5), 0.4, fill=True))
        plt.title("Circle")
        plt.show()


class Rectangle(Shape):
    def draw(self):
        fig, ax = plt.subplots()
        ax.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.6, fill=True))
        plt.title("Rectangle")
        plt.show()


class Triangle(Shape):
    def draw(self):
        fig, ax = plt.subplots()
        ax.add_patch(patches.Polygon([(0.5, 0.9), (0.1, 0.1), (0.9, 0.1)], fill=True))
        plt.title("Triangle")
        plt.show()


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.draw()
