# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Warehouse:
    # equipments = []
    def __init__(self, name):
        self.name = name
        self.equipments = []
    # Вот этот мне момент немного не ясен. Изначально я добавлял пустой список self.equipments = [] сразу как атрбут класса, но он становился как бы общим для всех
    # экземпляров. И при изменении списка в одном из них менялись списки и в других. Почему тогда такого не происходит с обычными не списочными атрибутами? Как
    # правильно тогда создать независимые списки для каждого экземпляра? Не уверен, что мой способ самый верный.

    def add_equipment(self, item):
        self.equipments.append(item)

    def replace_equipment(self, item, new_place):
        try:
            self.equipments.remove(item)
            new_place.add_equipment(item)
        except ValueError:
            print('Такого объекта нет на этом складе!')

    def get_filling(self):
        print(f'На складе \"{self.name}\" находится {len(self.equipments)} единиц техники')

    def __str__(self):
        self.get_filling()
        if len(self.equipments) > 0:
            for index,item in enumerate(self.equipments):
                print(f'Позиция {index+1}:')
                print(item)
            return ""
        else:
            return f'Склад {self.name} пуст'


class Equipment:
    def __init__(self,name):
        self.name = name

class Printer(Equipment):
    def __init__(self,name,print_size):
        super().__init__(name)
        self.print_size = print_size

    def __str__(self):
        return f'Принтер: {self.name}\nФормат печати: {self.print_size}'

    @staticmethod
    def new_equipment():
        name = input("Введите название: ")
        print_size = input("Введите размер печати: ")
        return Printer(name, print_size)

class Scaner(Equipment):
    def __init__(self,name,dpi):
        super().__init__(name)
        self.dpi = dpi

    def __str__(self):
        return f'Сканер: {self.name}\nРазрешение сканирования: {self.dpi}'

    @staticmethod
    def new_equipment():
        name = input("Введите название: ")
        dpi = input("Введите разрешение сканирования: ")
        return Scaner(name, dpi)

class Copier(Equipment):
    def __init__(self,name,speed):
        super().__init__(name)
        self.speed = speed

    def __str__(self):
        return f'Ксерокс: {self.name}\nСкорость копирования: {self.speed}'

    @staticmethod
    def new_equipment():
        name = input("Введите название: ")
        speed = input("Введите скорость копирования: ")
        return Copier(name, speed)

warehouses = [] #пока нет складов

# команды
commands = {'help': 'вывод доступных команд', 'add': 'добавить оборудование', 'move': 'переместить на другой склад', 'warehouse': 'проверить склад', 'exit': 'выйти'}

def new_equipment():
    while True:
        try:
            kind = int(input("Введине тип оборудования (1-принтер, 2-сканер, 3-ксерокс): "))
            if kind == 1:
                item = Printer.new_equipment()
                break
            if kind == 2:
                item = Scaner.new_equipment()
                break
            if kind == 3:
                item = Copier.new_equipment()
                break
            else:
                print("Введите число от 1 до 3")
        except ValueError:
            print("Введите число от 1 до 3")

    
    if len(warehouses) == 0:
        print('Доступных складлв нет. Приступаем к созданию.')
        new_warehouse().add_equipment(item)
    else:
        print("В какой склад добавить")
        text = list_of_warehouses()
        text += ', new - добавить новый: '
        place = input(text)
        if place == 'new':
            new_warehouse().add_equipment(item)
        else:
            warehouses[int(place)].add_equipment(item)

def new_warehouse():
    name = input('Введите назввание для склада: ')
    result = Warehouse(name)
    warehouses.append(result)
    return result

def check_warehouse():
    if len(warehouses) == 0:
        print('Склады не заведены!')
    else:
        print('Какой склад распечатать?')
        warehouses_index = input(f'{list_of_warehouses()}: ')
        print(warehouses[int(warehouses_index)])

def list_of_warehouses():
    result = [f'{index} - {warehouse.name}' for index,warehouse in enumerate(warehouses)]
    return ", ".join(result)

def list_of_equipments(warehouse):
    result = [f'{index} - {item.name}' for index,item in enumerate(warehouse.equipments)]
    return ", ".join(result)

def move_equipment():
    print('С какого склада забираем оборудование?')
    warehouse_1 = warehouses[int(input(f'{list_of_warehouses()}: '))]
    if len(warehouse_1.equipments) == 0:
        print('На выбранном складе нет оборудования!')
    else:
        print('Какое оборудование забираем?')
        item = warehouse_1.equipments[int(input(f'{list_of_equipments(warehouse_1)}: '))]
    print('На какой склада перемещаем оборудование?')
    warehouse_2 = warehouses[int(input(f'{list_of_warehouses()}: '))]
    warehouse_1.replace_equipment(item,warehouse_2)

def help():
    print("="*30)
    for key in commands.keys():
        print(f'{key} - {commands[key]}')
    print("="*30)

help()

while True:
    command = input("Введите команду: ")
    if command == 'exit':
        break
    elif command == 'add': 
        new_equipment()
    elif command == 'move':
        move_equipment()
    elif command == 'warehouse':
        check_warehouse()
    elif command == 'help':
        help()
    else:
        print("Команда не найдена")
    print("-"*30)