def game():
    print(f"{'Здравствуйте, Вас приветствует игра Крестики-Нолики!':^}")
    PLAYER_1 = input("Введите имя первого игрока:\n")
    PLAYER_2 = input("Введите имя второго игрока:\n")
    FIELD = []
    count = 1
    WIN_1 = 0
    WIN_2 = 0

    def made_field(n: int) -> list:
        """
        Функция создающая игровое поле заданного размерами N на N.
        :param n: целое число, принимает значение необходимого размера поля.
        :return:  elem: игровое поле типа список c количеством элементов N в квадрате.
        """
        elem = [["*" for _ in range(n)] for _ in range(n)]
        return elem

    def draw_field(field: list):
        """
        Функция позволяющая вывести игровое поле в виде матрицы.
        :return:
        """
        for _ in field:
            print(f"{_}")

    def motion(field: list, player: str) -> list:
        """
        Функция хода произведенного одним из игроков.
        :param field: список, образующий игровое поле.
        :param player: переменная, определяющая игрока чей ход осуществляется.
        :return: возвращает список, образующий игровое поле, с записанным ходом игрока.
        """
        print(f"Ходит игрок: {player.capitalize()}")
        while True:
            try:
                draw_field(FIELD)
                line = int(input("Введите номер строки необходимой ячейки:\n"))
                post = int(input("Введите номер столбца необходимой ячейки:\n"))
                if field[line][post] == "*":
                    if player == PLAYER_1:
                        field[line][post] = "X"
                    else:
                        field[line][post] = "O"
                    break
                else:
                    print(f"Данная ячейка уже занята, выберите свободную ячейку отмечанную символом *!")
                    continue
            except IndexError:
                print(f"Такой ячейки не существует! Вводите номера от 0 до {N - 1}!")
            except ValueError:
                print(f"Такой ячейки не существует! Вводите номера от 0 до {N - 1}!")
        return field

    def test_win(test_field: list, n: int) -> int:
        """
        Функция проверки уловия победы игрока
        :param test_field: список, содержащи игровое поле
        :param n: размер строки игрового поля
        :return: win: возвращает единицу в случае победы или ноль в случае отсутствия таковой.
        """

        win = 0
        a = [row[idx] for idx, row in enumerate(test_field)]
        # Cписок составленный из элементов диагонали "\" игрового поля
        b = [row[(n - 1) - idx] for idx, row in enumerate(test_field)]
        # Cписок составленный из элементов диагонали "/" игрового поля
        c = []
        d = []
        # Проверка победы по горизанталям и диагоналям:
        for k in test_field:
            if k.count("X") == n or a.count("X") == n or b.count("X") == n:
                draw_field(FIELD)
                print(f"!!!Поздравляю!!!\nПобедил игрок {PLAYER_1.capitalize()}!")
                win = 1
                break
            elif k.count("O") == n or a.count("O") == n or b.count("O") == n:
                draw_field(FIELD)
                print(f"!!!Поздравляю!!!\nПобедил игрок {PLAYER_2.capitalize()}!")
                win = 1
                break
        # Проверка победы по вертикалям:
        for k in range(0, n):
            for j in range(0, n - 1):
                if test_field[j][k] == test_field[abs(j - 1)][k] == test_field[j + 1][k] == "X":
                    c.append("X")
                elif test_field[j][k] == test_field[abs(j - 1)][k] == test_field[j + 1][k] == "O":
                    d.append("O")
            if c.count("X") == n - 1:
                draw_field(FIELD)
                print(f"!!!Поздравляю!!!\nПобедил игрок {PLAYER_1.capitalize()}!")
                win = 1
                break
            elif d.count("O") == n - 1:
                draw_field(FIELD)
                print(f"!!!Поздравляю!!!\nПобедил игрок {PLAYER_2.capitalize()}!")
                win = 1
                break
        return win

    # Выбор игрока для первого хода:
    while True:
        first_move = input("Кто будет ходить первым? Введите имя игрока:\n")
        if first_move.capitalize() == PLAYER_2.capitalize():
            PLAYER_1, PLAYER_2 = PLAYER_2, PLAYER_1
            break
        elif first_move.capitalize() == PLAYER_1.capitalize():
            break
        else:
            print("Такого игрока нет! Вы ввели неверное имя")
            continue

    # Создание игрового поля размерами N на N:
    while True:
        try:
            N = int(input("Введите желаемый размер строки игрового поля (не менее 3):\n"))
            if N >= 3:
                FIELD = made_field(N)
                break
            else:
                print("Вы ввели размер строки игрового поля менее 3!")
                continue
        except ValueError:
            print(f"Вы ввели неверное значение, размер сторки может быть только целым числом!")

    # Игра:
    while WIN_1 == 0 and WIN_2 == 0:
        motion(FIELD, PLAYER_1)
        WIN_1 = test_win(FIELD, N)
        count += 1
        if WIN_1 != 1 and count < (N ** 2):
            motion(FIELD, PLAYER_2)
            WIN_2 = test_win(FIELD, N)
            count += 1
        elif WIN_1 != 1 and WIN_2 != 1 and count >= (N ** 2):
            draw_field(FIELD)
            print("\n!!!Ничья!!!\n Победила дружба!")
            break

    new_game = "да"
    replay = input("Хотите сыграть еще раз (да / нет)?\n")
    if replay.lower() == new_game.lower():
        game()
    else:
        print("Игра закончена.\nДо новых встреч!!!")


game()
