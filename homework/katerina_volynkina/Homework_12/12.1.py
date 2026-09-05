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
    def __init__(self, name, color, lenght, freshness, life, cost):
        self.name = name
        self.color = color
        self.lenght = lenght
        self.freshness = freshness
        self.life = life
        self.cost = cost

    def __repr__(self):
        return (f"{self.name} (цвет - {self.color}, длина - {self.lenght}см, свежесть - {self.freshness}, "
                f"время жизни - {self.life}, стоимость - {self.cost})")


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

    def sort_freshness(self):
        sorted_freshness = sorted(self.flower, key=lambda f: f.freshness)
        return sorted_freshness

    def sort_color(self):
        sorted_color = sorted(self.flower, key=lambda f: f.color)
        return sorted_color

    def sort_lenght(self):
        sorted_lenght = sorted(self.flower, key=lambda f: f.lenght)
        return sorted_lenght

    def sort_cost(self):
        sorted_cost = sorted(self.flower, key=lambda f: f.cost)
        return sorted_cost

    def search_freshness(self, freshness):
        found_freshness= []
        for i in self.flower:
            if i.freshness == freshness:
                found_freshness.append(i)
        return found_freshness


flower_1 = Flowers("Роза", 'Красный', 30, "Свежий", 2, 500)
flower_2 = Flowers("Пион", 'Розовый', 25, "Увядший", 5, 300)
flower_3 = Flowers("Ромашка", 'Белый', 35, "Свежий", 6, 250)

my_buket = Buket()
my_buket.addition(flower_1)
my_buket.addition(flower_2)
my_buket.addition(flower_3)

print('Состав букета', my_buket.flower)
print('Среднее время увядания цветов в букете - ', my_buket.avg_life(), 'дня')
print(my_buket.sort_freshness())
print(my_buket.sort_color())
print(my_buket.sort_lenght())
print(my_buket.sort_cost())
print(my_buket.search_freshness("Свежий"))
