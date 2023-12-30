class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Невозможно уменьшить значение s!")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        min_moves = dx // self.s + dy // self.s
        if dx % self.s != 0 or dy % self.s != 0:
            min_moves += 1
        return min_moves
    
# Создаем объекты черепашки
t = Turtle(0, 0, 1)

# Перемещаемся и эволюционируем
t.go_right()
t.go_up()
t.evolve()

# Расчет минимального количества действий для достижения цели
min_moves = t.count_moves(4, 3)

print(f"Минимальное количество действий: {min_moves}")

# Проверка уменьшения значения s
t.degrade()
print(f"Значение s после уменьшения: {t.s}")

# Попытка уменьшить значение s до недопустимого значения
try:
    t.degrade()
except ValueError as e:
    print(f"Ошибка: {str(e)}")
