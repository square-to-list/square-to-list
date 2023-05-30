import asyncio

from square_to_list.square_to_list import get_matrix

SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
TRAVERSAL = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70,]


def test_get_matrix():
    # применение команды asyncio.run() дает ошибку RuntimeError: Event loop is closed
    # assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
    assert (
        asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL
    )
