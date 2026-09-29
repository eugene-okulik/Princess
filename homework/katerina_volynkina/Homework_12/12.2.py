# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.
# Для букета создать метод, который определяет время его увядания
# по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Flowers():
    def __init__(self, color, lenght, freshness, life):
        self.color = color
        self.lenght = lenght
        self.freshness = freshness
        self.life = life

    def __repr__(self):
        return (f"{self.name} (цвет - {self.color}, длина - {self.lenght}см, свежесть - {self.freshness}, "
                f"время жизни - {self.life}, стоимость - {self.cost})")


class Roses(Flowers):
    def __init__(self, name, color, lenght, freshness, life, cost):
        super().__init__(color, lenght, freshness, life)
        self.cost = cost
        self.name = name


class Pions(Flowers):
    def __init__(self, name, color, lenght, freshness, life, cost):
        super().__init__(color, lenght, freshness, life)
        self.cost = cost
        self.name = name


class Romashka(Flowers):
    def __init__(self, name, color, lenght, freshness, life, cost):
        super().__init__(color, lenght, freshness, life)
        self.cost = cost
        self.name = name


class Buket():
    def __init__(self):
        self.flower = []

    def addition(self, flowers_type):
        self.flower.append(flowers_type)

    def avg_life(self):
        total_life = 0
        for flower in self.flower:
            total_life += flower.life
        flowers_life = round(total_life / len(self.flower), 2)
        return flowers_life

# Женя посоветовал эту функцию сделать, вместо 4-х моих однотипных
    def sort_by(self, key):
        sorted_cost = sorted(self.flower, key=lambda f: getattr(f, key))
        return sorted_cost

    def search_freshness(self, freshness):
        found_freshness = []
        for i in self.flower:
            if i.freshness == freshness:
                found_freshness.append(i)
        return found_freshness

    def cost(self):
        cost = 0
        for i in self.flower:
            cost += i.cost
        return cost


flower_1 = Roses("Роза", 'Красный', 30, "Свежий", 2, 500)
flower_2 = Pions("Пион", 'Розовый', 25, "Увядший", 5, 300)
flower_3 = Romashka("Ромашка", 'Белый', 35, "Свежий", 6, 250)

my_buket = Buket()
my_buket.addition(flower_1)
my_buket.addition(flower_2)
my_buket.addition(flower_3)

print('Состав букета', my_buket.flower)
print('Среднее время увядания цветов в букете - ', my_buket.avg_life(), 'дня')
print(my_buket.sort_by("lenght"))  # и вот так она вызывается
print(my_buket.sort_by("color"))   # и вот так она вызывается
print(my_buket.search_freshness("Свежий"))
print('Стоимость всего букета -', my_buket.cost())
