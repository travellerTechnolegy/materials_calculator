"""Модуль для расчета площади и объема стены

Функции:
    - area(): возвращает площадь поверхности;
    - openings_area(): возвращает площадь проемов в стене;
    - wall_area(): возвращает площадь стены с учетом проемов;
    - wall_thickness(): возвращает толщину кладки стены;
    - wall_volume(): возвращает объем занимаемый стеною.
"""


def _area(dimensions: tuple[int, int]) -> int:
    """вычисляет площадь поверхности

    args:
        dimensions (tuple[int, int]): размеры стены
    returns:
        int: площадь в квадратных миллиметрах
    """
    return dimensions[0] * dimensions[1]


def _openings_area(openings: list[tuple[int, int]]) -> int:
    """вычисляет площадь проемов в стене

    args:
        openings (list[tuple[int, int]]): список кортежей проемов в стене

    returns:
        int: площадь в квадратных миллиметрах
    """
    open_area = 0
    for item in openings:        
        open_area += _area(item)
    return open_area


def wall_area(dimensions: tuple[int, int], openings:list[tuple[int, int]]) -> int:
    """вычисляет площадь стены с учетом проемов

    args:
        dimensions (tuple[int, int]): размеры стены
        openings (list[tuple[int, int]]): список кортежей проемов в стене


    returns:
        int: возвращает площадь стены с учетом проемов
    """
    return _area(dimensions) - _openings_area(openings)


def wall_thickness() -> int:
    """возвращает толщину кладки стены"""
    thicknesses = (120, 250, 380, 510, 640)
    promt = """Выберите толщину кладки:
    0 - 0,5 кирпича (120 мм)
    1 - 1 кирпич (250 мм)
    2 - 1,5 кирпича (380 мм)
    3 - 2 кирпича (510 мм)
    4 - 2,5 кирпича (640 мм)
    """
    thickness = int(input(f'{promt} \n --> '))
    print(f'Вы выбрали {thicknesses[thickness]}')
    return thicknesses[thickness]


def wall_volume(area: int, thickness: int) -> int:
    """вычисляет объем занимаемый стеною

    args:
        area (int): площадь стены
        thickness (int): толщина кладки

    returns:
        int: объем, занимаемый стеною
    """
    return area * thickness