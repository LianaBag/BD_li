Items = []
TVs = []
Notebooks = []
MWs = []
Monitors = []
Printers = []

Managers = []
Cashiers = []


class Technic:
    def __init__(self, model, price, condition=1):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 (не работает) или 1 (работает)
        """
        self.price = price
        self.condition = condition
        self.model = model

    def __str__(self):
        return 'Техника ' + self.model

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def test(self):
        return self.condition


class TV(Technic):
    def __init__(self, model, price, condition, w, h, t):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 или 1
        :param w: Ширина экрана
        :param h: Высота экрана
        :param t: Тип телевизора
        """
        Technic.__init__(self, model, price, condition)
        self.width = w
        self.height = h
        self.type = t

    def __str__(self):
        return Technic.__str__(self) + ' (телевизор)'

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Notebook(Technic):
    def __init__(self, model, price, condition, processor, ram, harddisk):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 или 1
        :param processor: Процессор
        :param ram: Кол-во оперативной памяти
        :param harddisk:  Кол-во памяти на жестком накопителе
        """
        Technic.__init__(self, model, price, condition)
        self.RAM = ram
        self.processor = processor
        self.diskSpace = harddisk

    def __str__(self):
        return Technic.__str__(self) + ' (ноутбук, ' + str(self.diskSpace) + 'ГБ)'

    def get_ram(self):
        return self.RAM

    def get_processor(self):
        return self.processor

    def get_disk_space(self):
        return self.diskSpace


class Microwave(Technic):
    def __init__(self, model, price, condition, power):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 или 1
        :param power: Мощность микроволновки в Ваттах
        """
        Technic.__init__(self, model, price, condition)
        self.power = power

    def __str__(self):
        return Technic.__str__(self) + ' (микроволновка, ' + str(self.power) + 'W)'

    def get_power(self):
        return self.power


class Printer(Technic):
    def __init__(self, model, price, condition, speed, format):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 или 1
        :param speed: Скорость печати л/мин
        :param format: Максимальный формат печати
        """
        Technic.__init__(self, model, price, condition)
        self.speed = speed
        self.format = format

    def __str__(self):
        return Technic.__str__(self) + ' (принтер, ' + str(self.format) + ')'

    def get_speed(self):
        return self.speed

    def get_format(self):
        return self.format


class Monitor(Technic):
    def __init__(self, model, price, condition, diagonal, freq):
        """
        :param model: Название модели
        :param price: Стоимость техники
        :param condition: Состояние: 0 или 1
        :param diagonal: диагональ экрана
        :param freq: частота обновления
        """
        Technic.__init__(self, model, price, condition)
        self.diagonal = diagonal
        self.freq = freq

    def __str__(self):
        return Technic.__str__(self) + ' (монитор, ' + str(self.diagonal) + '")'

    def get_diagonal(self):
        return self.diagonal

    def get_freq(self):
        return self.freq


class Worker:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def get_name(self):
        return self.name


class Cashier(Worker):
    def __init__(self, name, exp, busy):
        Worker.__init__(self, name, exp)
        self.busy = busy

    def is_busy(self):
        return self.busy

    def receipt(self, tech):
        print('Кассир: К оплате ', tech.get_price())


class Manager(Worker):

    def __init__(self, name, exp, dolgnost):
        Worker.__init__(self, name, exp)
        self.dolgnost = dolgnost

    def get_dolgnost(self):
        print(self.dolgnost)

    def test(self, tech, Consumer):
        if tech.test():
            self.sell(tech, Consumer)
        else:
            self.reject(tech, Consumer)

    def sell(self, tech, Consumer):
        print('Менеджер: ', tech, ' исправна, будете брать?')
        Consumer.proceed(tech, freeCashier())

    def reject(self, tech, Consumer):
        print('Менеджер: ', tech, ' неисправна')
        Consumer.reject()

    def show(self, type):
        if type == Notebook:
            s = 'ноутбуков'
            sr = Notebooks
        elif type == Printer:
            s = 'принтеров'
            sr = Printers
        elif type == TV:
            s = 'телевизоров'
            sr = TVs
        elif type == Monitor:
            s = 'мониторов'
            sr = Monitors
        elif type == Microwave:
            s = 'микроволновок'
            sr = MWs

        print('Менеджер: ', 'Вот список ', s)

        for item in sr:
            print(sr.index(item), ' ', item)


class Consumer:

    def __init__(self, name, Manager):
        self.name = name
        self.Manager = Manager

    def show(self, tech):
        self.Manager.show(tech)

    def choose(self, tech):
        print('Покупатель: ', 'Проверьте ', tech)
        self.Manager.test(tech, self)

    def reject(self):
        print('Покупатель: ', 'Жаль')

    def proceed(self, tech, cashier):
        print('Покупатель: ', 'Да')
        cashier.receipt(tech)
        print('Покупатель : *оплачивает и уходит*')


def add_item(tech):
    """ Добавление товара в магазин
    :param tech Объект класса Техника
    """
    if isinstance(tech, Technic):
        Items.append(tech)
        if isinstance(tech, TV):
            TVs.append(tech)
        elif isinstance(tech, Notebook):
            Notebooks.append(tech)
        elif isinstance(tech, Microwave):
            MWs.append(tech)
        elif isinstance(tech, Monitor):
            Monitors.append(tech)
        elif isinstance(tech, Printer):
            Printers.append(tech)
    return


def freeCashier():
    for c in Cashiers:
        if c.is_busy() is False:
            return c


add_item(TV('LG', 10000, 1, 1280, 720, 'обычный'))
add_item(TV('SAMSUNG', 25000, 0, 1600, 900, 'Smart'))
add_item(TV('Xiaomi', 35000, 1, 1920, 1080, 'TV2'))
add_item(TV('LG', 20000, 0, 1280, 1920, 'Smart'))
add_item(TV('SAMSUNG', 35000, 1, 1600, 900, 'обычный'))
add_item(TV('Xiaomi', 45000, 1, 720, 1080, 'TV2'))
add_item(Notebook('Xiaomi', 45000, 1, 'Intel i9', 8, 256))
add_item(Notebook('HP', 25000, 0, 'Intel Pentium', 4, 128))
add_item(Notebook('Predator', 100000, 1, 'AMD', 16, 1024))
add_item(Notebook('Xiaomi', 56000, 0, 'Intel Pentium', 8, 1024))
add_item(Notebook('Predator', 43000, 1, 'Intel i9', 4, 256))
add_item(Microwave('Canon', 5000, 1, 800))
add_item(Microwave('Daewoo', 3000, 0, 600))
add_item(Microwave('ЛОСь', 45000, 1, 1000))
add_item(Microwave('Canon', 8000, 1, 200))
add_item(Microwave('Daewoo', 6000, 1, 800))
add_item(Monitor('LG', 7500, 1, 22, 60))
add_item(Monitor('ЛОСь', 3500, 0, 23, 50))
add_item(Monitor('DELL', 8000, 1, 24, 75))
add_item(Monitor('LG', 8600, 0, 25, 80))
add_item(Monitor('ЛОСь', 4900, 1, 26, 65))
add_item(Monitor('DELL', 2000, 1, 27, 85))
add_item(Printer('HP', 3500, 0, 6, 'A4'))
add_item(Printer('Canon', 9000, 1, 14, 'A4'))
add_item(Printer('Epson', 15000, 1, 18, 'A3'))
add_item(Printer('Canon', 10000, 0, 6, 'A4'))
add_item(Printer('Epson', 8500, 0, 14, 'A3'))
add_item(Printer('HP', 18000, 1, 18, 'A3'))
Cashiers.append(Cashier('Вася', 1, False))
Cashiers.append(Cashier('Екатерина', 4, True))

Manager_A = Manager('Иванов И.И.', 0, 'стажер')
Manager_B = Manager('Сидоров С.С.', 2, 'младший')
Manager_C = Manager('Пупкин П.П.', 5, 'старший')

consumer = Consumer('Петрович', Manager_A)
print('Менеджер: Что ищите?\n 1 - Телевизоры\n 2 - Мониторы\n 3 - Принтеры\n 4 - Микроволновки\n 5 - Ноутбуки\n')
choise = input()
if (choise == '1'):
    consumer.show(TV)
    choise_ = input()
    consumer.choose(TVs[int(choise_)])
elif (choise == '2'):
    consumer.show(Monitor)
    choise_ = input()
    consumer.choose(Monitors[int(choise_)])
elif (choise == '3'):
    consumer.show(Printer)
    choise_ = input()
    consumer.choose(Printers[int(choise_)])
elif (choise == '4'):
    consumer.show(Microwave)
    choise_ = input()
    consumer.choose(MWs[int(choise_)])
elif (choise == '5'):
    consumer.show(Notebook)
    choise_ = input()
    consumer.choose(Notebooks[int(choise_)])
