class AddShipError(ValueError):
    pass


class TouchShip(AddShipError):
    pass


class ShipBeyondField(AddShipError):
    pass


class RepeateShot(ValueError):
    pass

class Field:
    size_field = 6

    def _get_header(self) -> str:
        result = "  "
        for x in range(1, self.size_field + 1):
            result += f"|{chr(64 + x)}"
        result += "|"
        return result
    
    def _get_marker(self, coord):
        value = self.field.get(coord)
        if value in self.shots and value == "■":
            value = 'X' 
        elif self.hid is False and value == "■":
            value = " "
        
        return value
        

    def __init__(self):
        self.field = {'1A': " ", '1B': " ", '1C': " ", '1D': " ", '1E': " ", '1F': " ",
                      '2A': " ", '2B': " ", '2C': " ", '2D': " ", '2E': " ", '2F': " ",
                      '3A': " ", '3B': " ", '3C': " ", '3D': " ", '3E': " ", '3F': " ",
                      '4A': " ", '4B': " ", '4C': " ", '4D': " ", '4E': " ", '4F': " ",
                      '5A': " ", '5B': " ", '5C': " ", '5D': " ", '5E': " ", '5F': " ",
                      '6A': " ", '6B': " ", '6C': " ", '6D': " ", '6E': " ", '6F': " "}
        self.occupied_points = []
        self.ship_on_field = []
        self.shots = []
        self.hid = True

    def __str__(self):
        return (f'{self._get_header()}\n'
                f'1 |{self._get_marker("1A")}|{self._get_marker("1B")}|{self._get_marker("1C")}|{self._get_marker("1D")}'
                f'|{self._get_marker("1E")}|{self._get_marker("1F")}|\n'
                f'2 |{self._get_marker("2A")}|{self._get_marker("2B")}|{self._get_marker("2C")}|{self._get_marker("2D")}'
                f'|{self._get_marker("2E")}|{self._get_marker("2F")}|\n'
                f'3 |{self._get_marker("3A")}|{self._get_marker("3B")}|{self._get_marker("3C")}|{self._get_marker("3D")}'
                f'|{self._get_marker("3E")}|{self._get_marker("3F")}|\n'
                f'4 |{self._get_marker("4A")}|{self._get_marker("4B")}|{self._get_marker("4C")}|{self._get_marker("4D")}'
                f'|{self._get_marker("4E")}|{self._get_marker("4F")}|\n'
                f'5 |{self._get_marker("5A")}|{self._get_marker("5B")}|{self._get_marker("5C")}|{self._get_marker("5D")}'
                f'|{self._get_marker("5E")}|{self._get_marker("5F")}|\n'
                f'6 |{self._get_marker("6A")}|{self._get_marker("6B")}|{self._get_marker("6C")}|{self._get_marker("6D")}'
                f'|{self._get_marker("6E")}|{self._get_marker("6F")}|\n')

    def add_ship(self, ship):  # по значению вызываем потом метод шип поинт
        try:
            for point in ship.ship_point():
                if point not in self.field:
                    raise ShipBeyondField('Корабль за пределами поля')
                if point in self.occupied_points:
                    raise TouchShip('Корабль задевает другой корабль')
        except AddShipError:
            raise AddShipError("Установите другой корабль")
        else:
            for point in ship.ship_point():  # для установки любого корабля
                self.field[point] = "■"
                self.occupied_points.append(point)
            self.ship_on_field.append(ship)

    def contur(self, ship, show=False):  # по значению вызываем потом метод шип поинт
        contour_dots = (
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        )

        for num, let in ship.ship_point():
            for x, y in contour_dots:
                number = chr(ord(num) + x)
                letter = chr(ord(let) + y)
                coord = number + letter
                if coord not in self.field:
                    continue
                if coord in self.occupied_points:
                    continue
                self.occupied_points.append(coord)
                if show:
                    self.field[coord] = '*'

    def shot(self, shot):
        if shot not in self.field:
            raise RepeateShot('Выстрел за пределами поля')
        if shot in self.occupied_points:
            raise RepeateShot('В эту точку уже стреляли')
        for i in self.ship_on_field:
            if shot in i.ship_point():
                print('Попал')
                self.field[shot] = 'X'
                if 1 < i.health:
                    print('Ранил... и людей на нем тоже')
                    i.health = i.health - 1
                    self.occupied_points.append(shot)
                    self.shots.append(shot)
                elif i.health == 1:
                    print('Уничтожил... а с моряками что?')
                    print('Верно! вокруг корабля плавают на обломках. Не стреляй туда')
                    self.occupied_points.append(shot)
                    self.shots.append(shot)
                    self.contur(i, show=True)
                return True
        print('Мимо')
        self.field[shot] = '*'
        self.shots.append(shot)
        self.occupied_points.append(shot)
        return False
        # тут должно быть предложение к повторению метода выстрела


class Ship:
    def __init__(self, first, end):
        self.first = first
        self.end = end
        self.health = len(self)

    def ship_point(self):
        ship = []
        if self.first[0] == self.end[0]:  # горизонтальнй кораблик
            for i in range(ord(self.first[1]), ord(self.end[1]) + 1):
                ship.append(self.first[0] + chr(i))
        elif self.first[1] == self.end[1]:  # верикальный кораблик, по аналогии с верхнем
            for i in range(int(self.first[0]), int(self.end[0]) + 1):
                ship.append(str(i) + self.first[1])
        return ship

    def __len__(self):
        return len(self.ship_point())
