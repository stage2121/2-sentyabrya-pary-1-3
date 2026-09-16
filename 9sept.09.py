# ЗАДАЧА 1

class Goods:
    title = "Мороженое"
    weight = 150
    tp = "Еда"
    price = 100


Goods.price = 2048
setattr(Goods, "inflation", 100)


# ЗАДАЧА 2

class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5
TravelBlog.total_blogs += 1

print(TravelBlog.total_blogs)


# ЗАДАЧА 3

class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("music.mp3")
media2.open("video.mp4")

media1.play()
media2.play()


# ЗАДАЧА 4

class Money:

    def __init__(self, money):
        self.money = money


my_money = Money(100)


# ЗАДАЧА 5

class Point:

    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


p1 = Point(10, 20)
p2 = Point(12, 5, "red")
p3 = Point(7, 15, "blue")

points = [p1, p2, p3]


# ЗАДАЧА 6

class DataBase:

    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data):
        values = data.split()
        item = dict(zip(self.FIELDS, values))
        self.lst_data.append(item)

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()

db.insert("1 Сергей 35 120000")
db.insert("2 Иван 28 90000")
db.insert("3 Анна 31 110000")
db.insert("4 Ольга 25 80000")

print(db.select(1, 3))


# ЗАДАЧА 7

class Graph:

    def __init__(self, data):
        self.data = data
        self.is_show = True

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


graph = Graph([1, 2, 3, 4, 5])

graph.show_table()

graph.set_show(False)
graph.show_table()


# ЗАДАЧА 8

class CPU:

    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:

    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = list(mem_slots[:4])

    def get_config(self):
        config = [
            f"Материнская плата: {self.name}",
            f"Процессор: {self.cpu.name}, частота: {self.cpu.fr}",
            f"Слотов памяти: {len(self.mem_slots)}"
        ]

        memory_info = []

        for mem in self.mem_slots:
            memory_info.append(f"{mem.name} - {mem.volume} ГБ")

        config.append("Память: " + ", ".join(memory_info))

        return config


cpu = CPU("Intel Core i5", 3.5)

mem1 = Memory("Kingston", 8)
mem2 = Memory("Samsung", 16)
mem3 = Memory("Kingston", 8)

board = MotherBoard(
    "ASUS Prime",
    cpu,
    mem1,
    mem2,
    mem3
)

for item in board.get_config():
    print(item)


# ЗАДАЧА 9

class Figure:

    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")


class Line(Figure):

    def draw(self):
        print("Рисуется линия")


class Rect(Figure):

    def draw(self):
        print("Рисуется прямоугольник")


class Ellipse(Figure):

    def draw(self):
        print("Рисуется эллипс")


class Triangle(Figure):

    def draw(self):
        print("Рисуется треугольник")


figures = [
    Line((0, 0, 10, 10), 2, "red"),
    Rect((0, 0, 20, 20), 3, "blue"),
    Ellipse((5, 5, 15, 15), 1, "green")
]

for figure in figures:
    figure.draw()

figures.append(
    Triangle((0, 0, 10, 20), 2, "yellow")
)

for figure in figures:
    figure.draw()
