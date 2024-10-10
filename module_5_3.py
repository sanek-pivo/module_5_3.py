class House:  # Создаем класс House
    def __init__(self, name, number_of_floors):  # используем метод init
        self.name = name  # присваиваем значение атрибутам
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): #Создаем метод go_to с параметром new_floor
        self.new_floor = new_floor
        number_of_floors = int(self.number_of_floors)

        if int(new_floor) > number_of_floors or int(new_floor) < 1:  # сравнение new_floor и чем self.number_of_floors
            print('Такого этажа не существует')
        else:
            floor = 0
            for floor in range(0, new_floor):  # перебираем количество этажей
                floor = floor + 1
                print(floor)
            return floor

        def __len__(self):
            return self.nFloors

        def __str__(self):
            return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'
         # дополним  класс House следующими специальными методами:
        def __eq__(self,other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors == other.number_of_floors

        def __it__(self,other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors < other.number_of_floors

        def __le__(self,Other):
            if isinstance(other.number_of_floors, int) and isinstance(other, House):
                return self.number_of_floors <= other.number_of_floors

        def __gt__(self, Other):
            def __le__(self, Other):
                return self.number_of_floors > other.number_of_floors

        def __ge__(self, Other):
            def __le__(self, Other):
                return self.number_of_floors => other.number_of_floors

        def __ne__(self, Other):
            def __le__(self, Other):
                return self.number_of_floors != other.number_of_floors

        def __add__(self,value):
            if isinstance(value, int):
                self.number_of_floors = self.number_of_floors + value
            return self

        def __radd__(self, value):
            return self.__add__(value)

        def __iadd__(self,Value):
            if isinstance(value, int):
                self.number_of_floors += value
                return self
    # выводим результаты по домашнему заданию
        h1 = House('ЖК Эльбрус', 10)
        h2 = House('ЖК АКация', 20)

        print(h1)
        print(h2)
        print(h1 == h2)
        print(h1.__add__(10))
        print(h1 == h2)
        print(h1.__add__(10))
        print(h2.__add__(10))
        print(h1 < h2)
        print(h1 <= h2)
        print(h1 > h2)
        print(h1 >= h2)
        print(h1 != h2)

