"""Модуль для получения исходных данных и выдачи результа расчета количества кирпичей в стене с 
учетом проемов (окна, двери) и необходимого для кладки объема раствора.

Функции:
    - get_brick_size(): возвращает размеры выбранного кирпича;
    - get_wall_openings(): возвращает список кортежей из размеров проемов в стене;
    - get_wall_dimensions(): возвращает размеры стены;
    - main(): инициализирует запуск калькулятора, ввод данных, их обработку и вывод на экран.
"""


from wall import *
from material import *


def get_brick_size() -> tuple[int, int, int]:
    """возвращает размеры выбранного кирпича
    """
    sizes = [(250, 120, 65), (250, 120, 88), (250, 120, 138)]
    promt = """Выберите размер кирпича:
    0 - одинарный (250*120*65)
    1 - полуторный (250*120*88)
    2 - двойной (250*120*138)
    """
    size = int(input(f'{promt} \n --> '))
    print(f'Вы выбрали {sizes[size]}')
    return sizes[size]


def get_wall_openings() -> list[tuple[int, int]]: 
    """возвращает список кортежей из размеров проемов в стене
    """   
    ask = int(input("Есть в стене проёмы?, (да - 1, нет - 0): "))
    if not ask:
        return [(0, 0)]
    list_openings = [] 
    while True:
        length = int(input("Введите длину проема (мм): "))
        height = int(input("Введите высоту проема (мм): "))
        list_openings.append((length, height))
        ask = int(input("Ещё есть проёмы?, (да - 1, нет - 0): "))
        if not ask:
            return list_openings


def get_wall_dimensions() -> tuple[int, int]:
    """возвращает размеры стены, мм

    returns:
        -length: int,
        -height: int
    """
    length = int(input("Введите длину стены (мм): "))
    height = int(input("Введите высоту стены (мм): "))
    return length, height


def main():
    """инициализирует запуск калькулятора, ввод данных, их обработку и вывод на экран.
    """
    dimensions = get_wall_dimensions()
    openings = get_wall_openings()
    area = wall_area(dimensions, openings)
    thickness = wall_thickness()
    volume = wall_volume(area, thickness)
    brik_size = get_brick_size()
    x, y = amount_of_material(volume, brik_size)
    print(f"Количество кирпичей в стене - {x} шт.")
    print(f"Объем раствора в стене - {y} м куб")



if __name__ == "__main__":
    main()






