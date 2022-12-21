from decouple import config
from game_entity import game
print('Вас приветствует Казино Tilek')
print(f'Ваш депозит 1000$')

my_money = config('MY_MONEY', cast=int)
while True:
    print(f'Текущий баланс {my_money}')
    user_bet = int(input('Выберите целое число от 1 до 30: '))
    stake = int(input('Сделайте ставку: '))
    win = int(game(user_bet, stake))
    my_money = my_money - stake + win
    if win != 0:
        print(f'Поздравляем!!! Ваш выигрыш {win}')
    elif win == 0:
        print('Не повезло, попробуйте еще раз.')
    user_say = int(input("Для продолжения введите '1', для выхода введите '2': "))
    if user_say == 1:
        continue
    if user_say == 2:
        print("Вы вышли из игры!!!")
        break
