import asyncio

import aiohttp


def square_str_to_square_list(square_str: str) -> list:
    """
    function is converting a square matrix (NxN) from a Str to a List[List[int]]
    :param str:
    :return list:
    """
    square_list = []
    line = []
    num = []
    for i in range(1, len(square_str)):
        if square_str[i].isdigit():
            num.append(square_str[i])
            if not square_str[i + 1].isdigit():
                line.append(int("".join(num)))
                num = []
                if square_str[i + 4] == "+":
                    square_list.append(line)
                    line = []
    return square_list


def square_list_to_line_list(square_list: list) -> list:
    """
    function is converting a square matrix (NxN) from a List[List[int]] to
    List[int] as a result of traversing the original matrix
    in a counterclockwise spiral, starting from the upper left corner
    :param list:
    :return list:
    """
    line_list = []
    while len(square_list):
        if len(square_list) > 1:
            for i in range(0, len(square_list) - 1):
                line_list.append(square_list[i].pop(0))
            line_list.extend(square_list.pop(-1))
            for i in reversed(range(0, len(square_list))):
                line_list.append(square_list[i].pop())
            square_list[0].reverse()
            line_list.extend(square_list.pop(0))
        else:
            line_list.extend(square_list.pop())
    return line_list


async def get_matrix(url: str) -> list[int]:
    """
    function is getting a square matrix (NxN) from a remote server by URL and
    returns it as a List[int] as a result of traversing the original matrix
    in a counterclockwise spiral, starting from the upper left corner
    :param url:
    :return list[int]:
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    square_str = await response.content.read()
                    square_str = square_str.decode("utf-8")
                else:
                    return f'Error {response.status}: {await response.text()}'
    except Exception as exc:
        return exc

    square_list = square_str_to_square_list(square_str)
    line_list = square_list_to_line_list(square_list)

    return line_list


if __name__ == "__main__":
    SOURCE_URL = input("Input URL: ")
    if SOURCE_URL == "":
        SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
        print("You did not input a matrix URL, so the testing URL will be applied.")
    # line_list = asyncio.run(get_matrix(SOURCE_URL))
    # command: asyncio.run() gives the errror -> RuntimeError: Event loop is closed
    line_list = asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL))
    print(line_list)
