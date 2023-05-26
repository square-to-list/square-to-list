from square_to_list.square_to_list import (
    square_str_to_square_list,
    square_list_to_line_list,
)


def test_square_str_to_square_list():
    square_str = (
        "+-----+-----+-----+-----+ |  10 |  20 |  30 |  40 | +-----+-----+-----+-----+"
        "|  50 |  60 |  70 |  80 | +-----+-----+-----+-----+ |  90 | 100 | 110 | 120 | "
        "+-----+-----+-----+-----+ | 130 | 140 | 150 | 160 | +-----+-----+-----+-----+ "
    )
    print(square_str)
    square_list = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]
    assert square_str_to_square_list(square_str) == square_list


def test_square_list_to_line_list():
    square = [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
        [130, 140, 150, 160],
    ]
    line = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
    assert square_list_to_line_list(square) == line
