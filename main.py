import random
import copy


class Playing_field:  # класс - игровое поле
    def __init__(self):
        self.field = [[' . ' for i in range(10)] for x in range(10)]  # расположение кораблей на поле
        self.ships1 = []  # списки кораблей
        self.ships2 = []
        self.ships3 = []
        self.ships4 = []

    def __str__(self):
        res = '\n'.join(''.join(el for el in elem) for elem in self.field)
        return res

    def key_field(self):  # передача расположения кораблей
        return self.field

    def arrange_the_ships(self):  # метод генерации положения кораблей
        done = 0  # 4-палубный
        while done == 0:
            x, y = random.randint(0, 9), random.randint(0, 9)
            rotate = random.randint(0, 1)
            if rotate == 0 and 0 <= x + 3 <= 9:  # горизонтально
                for i in range(x, x + 4):
                    self.field[y][i] = ' X '
                done = 1
                self.ships4.append((x, y, 'right'))
            if rotate == 1 and 0 <= y + 3 <= 9:  # вертикально
                for i in range(y, y + 4):
                    self.field[i][x] = ' X '
                done = 1
                self.ships4.append((x, y, 'down'))
        for i in range(2):  # 3-палубные
            done = 0
            while done == 0:
                x, y = random.randint(0, 9), random.randint(0, 9)
                rotate = random.randint(0, 1)
                if rotate == 0:  # горизонтально
                    x1 = x + 2
                    if 0 <= x1 <= 9:  # проверка, что координаты не вышли за пределы допустимых значений
                        if self.field[y][x] == ' . ' and self.field[y][x + 1] == ' . ' \
                                and self.field[y][x + 2] == ' . ':  # проверка, что в выбранных клетках нет корабля
                            if (y != 0 and self.field[y - 1][x] == ' . ' and self.field[y - 1][x + 1] == ' . '
                                and self.field[y - 1][x + 2] == ' . ') or y == 0:  # проверка сверху
                                if (y != 9 and self.field[y + 1][x] == ' . ' and self.field[y + 1][x + 1] == ' . '
                                    and self.field[y + 1][x + 2] == ' . ') or y == 9:  # проверка снизу
                                    if (x != 0 and self.field[y][x - 1] == ' . ') or x == 0:  # проверка слева
                                        if (x1 != 9 and self.field[y][x1 + 1] == ' . ') or x1 == 9:  # проверка справа
                                            if (x == 0
                                                or y == 0) or (x != 0 and y != 0
                                                               and self.field[y - 1][x - 1] == ' . '):  # верх.лев угол
                                                if (x1 == 9 or y == 9) \
                                                        or (x1 != 9 and y != 9
                                                            and self.field[y + 1][x1 + 1] == ' . '):  # ниж.прав угол
                                                    if (x1 == 9 or y == 0) \
                                                            or (x1 != 9 and y != 0
                                                                and self.field[y - 1][x1 + 1] == ' . '):  # верх.прав
                                                        if (x == 0 or y == 9) \
                                                                or (x != 0 and y != 9
                                                                    and self.field[y + 1][x - 1] == ' . '):  # ниж.лев
                                                            done = 1
                                                            self.ships3.append((x, y, 'right'))
                                                            for j in range(x, x1 + 1):
                                                                self.field[y][j] = ' X '
                if rotate == 1:  # вертикально
                    y1 = y + 2
                    if 0 <= y1 <= 9:  # проверка, что координаты не вышли за пределы допустимых значений
                        if self.field[y][x] == ' . ' and self.field[y + 1][x] == ' . ' \
                                and self.field[y + 2][x] == ' . ':  # проверка, что в выбранных клетках нет корабля
                            if (x != 0 and self.field[y][x - 1] == ' . ' and self.field[y + 1][x - 1] == ' . '
                                and self.field[y + 2][x - 1] == ' . ') or x == 0:  # проверка слева
                                if (x != 9 and self.field[y][x + 1] == ' . ' and self.field[y + 1][x + 1] == ' . '
                                    and self.field[y + 2][x + 1] == ' . ') or x == 9:  # проверка справа
                                    if (y != 0 and self.field[y - 1][x] == ' . ') or y == 0:  # проверка сверху
                                        if (y1 != 9 and self.field[y1 + 1][x] == ' . ') or y1 == 9:  # проверка снизу
                                            if (x == 0 or y == 0) \
                                                    or (x != 0 and y != 0
                                                        and self.field[y - 1][x - 1] == ' . '):  # верх.лев.
                                                if (x == 9 or y1 == 9) \
                                                        or (x != 9 and y1 != 9
                                                            and self.field[y1 + 1][x + 1] == ' . '):  # ниж.прав.
                                                    if (x == 9 or y == 0) \
                                                            or (x != 9 and y != 0
                                                                and self.field[y - 1][x + 1] == ' . '):  # верх.прав.
                                                        if (x == 0 or y1 == 9) \
                                                                or (x != 0 and y1 != 9
                                                                    and self.field[y1 + 1][x - 1] == ' . '):  # ниж.лев.
                                                            done = 1
                                                            self.ships3.append((x, y, 'down'))
                                                            for j in range(y, y1 + 1):
                                                                self.field[j][x] = ' X '
        for i in range(3):  # 2-палубные
            done = 0
            while done == 0:
                x, y = random.randint(0, 9), random.randint(0, 9)
                rotate = random.randint(0, 1)
                if rotate == 0:  # горизонтально
                    x1 = x + 1
                    if 0 <= x1 <= 9:  # проверка, что координаты не вышли за пределы допустимых значений
                        if self.field[y][x] == ' . ' and self.field[y][x + 1] == ' . ':  # в выбранных клетках пусто
                            if (y != 0 and self.field[y - 1][x] == ' . ' and self.field[y - 1][x + 1] == ' . ') \
                                    or y == 0:  # проверка сверху
                                if (y != 9 and self.field[y + 1][x] == ' . ' and self.field[y + 1][x + 1] == ' . ') \
                                        or y == 9:  # проверка снизу
                                    if (x != 0 and self.field[y][x - 1] == ' . ') or x == 0:  # проверка слева
                                        if (x1 != 9 and self.field[y][x1 + 1] == ' . ') or x1 == 9:  # проверка справа
                                            if (x == 0 or y == 0) \
                                                    or (x != 0 and y != 0
                                                        and self.field[y - 1][x - 1] == ' . '):  # верх.лев угол
                                                if (x1 == 9 or y == 9) \
                                                        or (x1 != 9 and y != 9
                                                            and self.field[y + 1][x1 + 1] == ' . '):  # ниж.прав угол
                                                    if (x1 == 9 or y == 0) \
                                                            or (x1 != 9 and y != 0
                                                                and self.field[y - 1][x1 + 1] == ' . '):  # верх.прав
                                                        if (x == 0 or y == 9) \
                                                                or (x != 0 and y != 9
                                                                    and self.field[y + 1][x - 1] == ' . '):  # ниж.лев
                                                            done = 1
                                                            self.ships2.append((x, y, 'right'))
                                                            for j in range(x, x1 + 1):
                                                                self.field[y][j] = ' X '
                if rotate == 1:  # вертикально
                    y1 = y + 1
                    if 0 <= y1 <= 9:  # проверка, что координаты не вышли за пределы допустимых значений
                        if self.field[y][x] == ' . ' and self.field[y + 1][x] == ' . ':  # в выбранных клетках пусто
                            if (x != 0 and self.field[y][x - 1] == ' . '
                                and self.field[y + 1][x - 1] == ' . ') or x == 0:  # проверка слева
                                if (x != 9 and self.field[y][x + 1] == ' . '
                                    and self.field[y + 1][x + 1] == ' . ') or x == 9:  # проверка справа
                                    if (y != 0 and self.field[y - 1][x] == ' . ') or y == 0:  # проверка сверху
                                        if (y1 != 9 and self.field[y1 + 1][x] == ' . ') or y1 == 9:  # проверка снизу
                                            if (x == 0 or y == 0) \
                                                    or (x != 0 and y != 0
                                                        and self.field[y - 1][x - 1] == ' . '):  # верх.лев.
                                                if (x == 9 or y1 == 9) \
                                                        or (x != 9 and y1 != 9
                                                            and self.field[y1 + 1][x + 1] == ' . '):  # ниж.прав.
                                                    if (x == 9 or y == 0) \
                                                            or (x != 9 and y != 0
                                                                and self.field[y - 1][x + 1] == ' . '):  # верх.прав.
                                                        if (x == 0 or y1 == 9) \
                                                                or (x != 0 and y1 != 9
                                                                    and self.field[y1 + 1][x - 1] == ' . '):  # ниж.лев.
                                                            done = 1
                                                            self.ships2.append((x, y, 'down'))
                                                            for j in range(y, y1 + 1):
                                                                self.field[j][x] = ' X '
        for i in range(4):  # 1-палубные
            done = 0
            while done == 0:
                x, y = random.randint(0, 9), random.randint(0, 9)
                if self.field[y][x] == ' . ':  # в выбранных клетках пусто
                    if (y != 0 and self.field[y - 1][x] == ' . ') or y == 0:  # проверка сверху
                        if (y != 9 and self.field[y + 1][x] == ' . ') or y == 9:  # проверка снизу
                            if (x != 0 and self.field[y][x - 1] == ' . ') or x == 0:  # проверка слева
                                if (x != 9 and self.field[y][x + 1] == ' . ') or x == 9:  # проверка справа
                                    if (x == 0 or y == 0) \
                                            or (x != 0 and y != 0 and self.field[y - 1][x - 1] == ' . '):  # верх.лев
                                        if (x == 9 or y == 9) \
                                                or (x != 9 and y != 9 and self.field[y + 1][x + 1] == ' . '):  # ниж.пр
                                            if (x == 9 or y == 0) or (x != 9 and y != 0
                                                                      and self.field[y - 1][x + 1] == ' . '):  # верх.пр
                                                if (x == 0 or y == 9) or (x != 0 and y != 9
                                                                          and self.field[y + 1][x - 1] == ' . '):  # н.л
                                                    done = 1
                                                    self.field[y][x] = ' X '
                                                    self.ships1.append((x, y))


class Sea_Battle:  # класс игры "морской бой"
    def __init__(self):
        self.PF = Playing_field()
        self.PF.arrange_the_ships()
        self.player_field = [[' = ' for i in range(10)] for x in range(10)]  # поле игрока, на нём будут видны ходы
        self.ships = len(self.PF.ships4) + len(self.PF.ships3) + len(self.PF.ships2) + len(self.PF.ships1)  # к-во
        # не уничтоженных кораблей

    def __str__(self):
        res = '    A  B  C  D  E  F  G  H  I  J' + '\n'
        pfnums = copy.deepcopy(self.player_field)
        for i in range(9):
            pfnums[i].insert(0, ' ' + str(i + 1) + ' ')
        pfnums[9].insert(0, '10 ')
        res += '\n'.join(''.join(el for el in elem) for elem in pfnums)
        return res

    def Move(self):  # ХОД ИГРОКА - выстрел по клеткам поля
        done = False
        print('Введите координаты выстрела (формат ввода - G9)')
        while done is False:
            shot = input()
            x, y = shot[0], shot[1::]
            if x in 'ABCDEFGHIJ' and y.isnumeric() and 1 <= int(y) <= 10:
                y = int(y) - 1
                if self.player_field[y][ord(x) - 65] != ' = ':
                    print("По этим координатам уже производился выстрел")
                else:
                    done = True
            else:
                print("Неверный формат ввода")
        x = ord(x) - 65
        if self.PF.key_field()[y][x] == ' X ':
            self.player_field[y][x] = ' X '  # фиксация попадания
            print("ПОПАДАНИЕ!")
            # проверка на поражение всего корабля
            delete = 0
            for coord in self.PF.ships4:  # проверка линкоров
                x, y, rotate = coord
                if rotate == 'right' and self.player_field[y][x] == ' X ' and self.player_field[y][x + 1] == ' X ' \
                        and self.player_field[y][x + 2] == ' X ' and self.player_field[y][x + 3] == ' X ':
                    delete = (x, y, rotate)
                if rotate == 'down' and self.player_field[y][x] == ' X ' and self.player_field[y + 1][x] == ' X ' \
                        and self.player_field[y + 2][x] == ' X ' and self.player_field[y + 3][x] == ' X ':
                    delete = (x, y, rotate)
            if delete != 0:
                self.PF.ships4.remove(delete)
                print("Вы уничтожили линкор!")
            delete = 0
            for coord in self.PF.ships3:  # проверка крейсеров
                x, y, rotate = coord
                if (rotate == 'right' and self.player_field[y][x] == ' X ' and self.player_field[y][x + 1] == ' X '
                    and self.player_field[y][x + 2] == ' X ') \
                        or (rotate == 'down' and self.player_field[y][x] == ' X '
                            and self.player_field[y + 1][x] == ' X ' and self.player_field[y + 2][x] == ' X '):
                    delete = (x, y, rotate)
            if delete != 0:
                self.PF.ships3.remove(delete)
                print("Вы уничтожили крейсер!")
            delete = 0
            for coord in self.PF.ships2:  # проверка эсминцев
                x, y, rotate = coord
                if (rotate == 'right' and self.player_field[y][x] == ' X ' and self.player_field[y][x + 1] == ' X ') \
                        or (rotate == 'down' and self.player_field[y][x] == ' X '
                            and self.player_field[y + 1][x] == ' X '):
                    delete = (x, y, rotate)
            if delete != 0:
                self.PF.ships2.remove(delete)
                print("Вы уничтожили эсминца!")
            delete = 0
            for coord in self.PF.ships1:  # проверка торпедных катеров
                x, y = coord
                if self.player_field[y][x] == ' X ':
                    delete = (x, y)
            if delete != 0:
                self.PF.ships1.remove(delete)
                print("Вы уничтожили торпедный катер!")
        else:
            print("промах")
            self.player_field[y][x] = ' . '
        self.Show_position()

    def Start(self):  # запуск игры
        self.Show_position()
        while self.Check_Win() is False:
            self.Move()

    def Show_position(self):  # метод показа игрового поля
        print(self)

    def Check_Win(self):  # проверка на выигрыш (оставшиеся корабли)
        self.ships = len(self.PF.ships4) + len(self.PF.ships3) + len(self.PF.ships2) + len(self.PF.ships1)
        if self.ships == 0:
            print("ВЫ ВЫИГРАЛИ!")
            return True
        else:
            return False


Game = Sea_Battle()
#  print(Game.PF)  # расположение кораблей
Game.Start()
