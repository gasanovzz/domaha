import random


class Card:
    def __init__(self, name):
        bag = [x for x in range(1, 91)]
        self.card = [__class__.gen_string(bag), __class__.gen_string(bag),
                     __class__.gen_string(bag)]
        self.name = name
        self.count_barrel = 15

    @staticmethod
    def gen_string(bag):
        string = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            digit = random.randint(0, x)
            while string[digit] != '':
                digit += 1
            string[digit] = bag.pop(random.randint(0, len(bag) - 1))
        return string

    def __str__(self):
        rez = '{:-^26}\n'.format(self.name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return rez + '--------------------------'

computer = Card(' Карточка компьютера ')
player = Card(' Карточка игрока ')
bag = [x for x in range(1, 91)]  # Мешок с бочками.
while True:
    if len(bag) < 1:
        print('Бочонки закончились. Результат:\n'
              'у компьютера осталось {} числа/чисел,\n'
              'у игрока осталось {} числа/чисел.'
              .format(computer.count_barrel, player.count_barrel))
        break
    barrel = bag.pop(random.randint(0, len(bag) - 1))
    print('\nНовый бочонок: {} (осталось {})'.format(barrel, len(bag)))
    print(computer)
    print(player)
    reply = input('Зачеркнуть цифру? (y/n/q)')
    reply = reply.lower()
    while len(reply) == 0 or reply not in 'ynq':
        print('\n\nПРИНИМАЮТСЯ ТОЛЬКО ОТВЕТЫ В ФОРМАТЕ Y(YES) N(NO) Q(QUIT)\n')
        print('Новый бочонок: {} (осталось {})'.format(barrel, len(bag)))
        print(computer)
        print(player)
        reply = input('Зачеркнуть цифру? (y/n/q)')
        reply = reply.lower()

    if reply == 'q':
        print('Игра закончена')
        break
    elif reply == 'y':
        test = False  # Есть ли такая цифра на карточке игрока?
        for x in range(3):
            if barrel in player.card[x]:
                test = True
                player.card[x][player.card[x].index(barrel)] = '-'
                player.count_barrel -= 1
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            if player.count_barrel < 1:
                print('Похоже, вы выиграли')
                break
            elif computer.count_barrel < 1:
                print('Вы проиграли компьютеру, задумайтесь о своей жизни')
                break
        else:
            print('Игра закончена, не жульничайте')
            break
    elif reply == 'n':
        test = False
        for x in range(3):
            if barrel in player.card[x]:
                print('Игра закончена, данной число присутсвует на вашей карточке')
                test = True
                break
            if barrel in computer.card[x]:
                computer.card[x][computer.card[x].index(barrel)] = '-'
                computer.count_barrel -= 1
        if test:
            break
        if player.count_barrel < 1:
            print('Поздравляем, Ваша победа прекрасна как цветующая сакура')
            break
        elif computer.count_barrel < 1:
            print('Вы проиграли компьютеру, задумайтесь о своей жизни')
            break