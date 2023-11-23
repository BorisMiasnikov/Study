
import random
from Sea_battle import AddShipError, Ship, Field, RepeateShot
class Player:
    def __init__(self, user, enemy):
        self.user_field = user
        self.enemy_field = enemy
    def ask(self):
        raise NotImplemented
    def move(self):
        try:
            point = self.ask()
            x = self.enemy_field.shot(point)
        except RepeateShot as e:
            print(e)
            print('Сделайте выстрел повторно')
            return self.move()
        return x

        #     if x:
        #         self.move()

class User(Player):
    def ask(self):
        print('Ходит человек')
        x = input()
        return x



class AI(Player):
    def ask(self):
        x = random.choice(list(self.enemy_field.field.keys()))
        print(f'ходит компьютер, {x}')
        return x


class Game:
    def __init__(self):
        user_field = self.random_field()
        ai_field = self.random_field()
        ai_field.hid = False
        self.user = User(user_field, ai_field)
        self.ai = AI(ai_field, user_field)

    def random_field(self) -> Field:
        ships = [(3, 1), (2, 2), (1, 4)]
        result = Field()
        value = 1
        for size, count in ships:
            for i in range (1,count+1):
                while True:
                    if value <=100:
                        value += 1
                        rand_x_start = random.randint(1, result.size_field)
                        rand_y_start = random.randint(1, result.size_field)
                        if random.random() > 0.5:
                            rand_x_end = rand_x_start + size-1
                            rand_y_end = rand_y_start
                        else:
                            rand_x_end = rand_x_start
                            rand_y_end = rand_y_start + size-1
                        start = f"{rand_y_start}{chr(64+rand_x_start)}"
                        end = f"{rand_y_end}{chr(64+rand_x_end)}"

                        try:
                            ship = Ship(start, end)
                            result.add_ship(ship)
                            result.contur(ship)
                        except AddShipError:
                            continue
                        else:
                            break
                    else:
                        return self.random_field()
        result.occupied_points = []
        return result

    def greet(self):
        print('Приветствую на игре Морской бой \n'
              'Начинать игру будет пользоватль - Вы! \n'
              'Против самого умного компьютера \n'
              'Чтобы совершить выстрел нужно ввести значение клетки\n'
              'в формате цифра/буква например 1В,(не привычно, но так получилось) используя ENG раскладку')


    def loop(self):
        is_user_move = True
        while  ("■" in list(self.user.user_field.field.values())) and ("■" in list(self.ai.user_field.field.values())):
            print(self.user.user_field)
            print(self.ai.user_field)
            if is_user_move:
                result = self.user.move()
            else:
                result = self.ai.move()
            if not result:
                is_user_move = not is_user_move
        if "■" not in list(self.user.user_field.field.values()):
            print('победил ai')
            print(self.user.user_field)
        elif "■" not in list(self.ai.user_field.field.values()):
            print('Победил игрок')
            print(self.ai.user_field)



    def start(self):
        self.greet()
        self.loop()
game = Game()
game.start()









