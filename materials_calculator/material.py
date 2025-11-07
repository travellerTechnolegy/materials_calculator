"""Модуль для расчета количества материала используемого для 
кладки стены: кирпича (шт.) и раствора (метры кубические).

Функции:
    - brick_volume(): возвращает объем одного кирпича ( миллиметры кубические);
    - brick_volume_stitch(): возвращает обем кирпича с учетом растворного шва (по умолчанию шов равен 10 мм);
    - amount_of_materia(): возвращает количество кирпичей (шт.) и объем раствора (метры кубические).
"""


from math import ceil


def _brick_volume(brik_size: tuple[int, int, int]) -> int:
    """вычисляет объем одного кирпича

    args:
        brik_size (tuple[int, int, int]): размеры кирпича

    returns:
        int: объем одного кирпича
    """
    return brik_size[0] * brik_size[1] * brik_size[2]


def _brick_volume_stitch(brik_size: tuple[int, int, int], stitch: int) -> int:
    """возвращает обем кирпича с учетом растворного шва 
    Args:
        brik_size (tuple[int, int, int]): размер кирпича
        stitch (int): растворный шов, по умолчанию равен 10 мм

    Returns:
        int: обем кирпича с учетом растворного шва
    """
    brick_size_stitch = []
    for item in brik_size:
        brick_size_stitch.append(item + stitch)
    return brick_size_stitch[0] * brick_size_stitch[1] * brick_size_stitch[2]


def amount_of_material(volume: int, brik_size: tuple[int, int, int], stitch=10) -> tuple[float, float]:
    """вычисляет количество кирпичей (шт.) и объем раствора (метры кубические)

    Args:
        volume (int): объем стены, мм куб
        brik_size (tuple[int, int, int]): размеры кирпича
        stitch (int, optional): Растворный шов. Defaults to 10.

    Returns:
        tuple[float, float]: количество кирпичей и раствора с 5% надбавкой
    """
    number_of_bricks = ceil((volume / _brick_volume_stitch(brik_size, stitch)) * 1.05)
    volume_of_solution = round(((volume/_brick_volume(brik_size) - number_of_bricks) * _brick_volume(brik_size) / 10**9) * 1.05, 2)
    return number_of_bricks, volume_of_solution

