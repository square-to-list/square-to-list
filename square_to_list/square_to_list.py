import aiohttp
import asyncio


def square_str_to_square_list(s):
    f = []
    m = []
    k = []
    for i in range(1, len(s)):
        if s[i].isdigit():
            k.append(s[i])
            if not s[i + 1].isdigit():
                m.append(int("".join(k)))
                k = []
                if s[i + 4] == "+":
                    f.append(m)
                    m = []
    return f


def square_list_to_line_list(f):
    e = []
    while len(f):
        if len(f) > 1:
            for i in range(0, len(f) - 1):
                e.append(f[i].pop(0))
            e.extend(f.pop(-1))
            for i in reversed(range(0, len(f))):
                e.append(f[i].pop())
            f[0].reverse()
            e.extend(f.pop(0))
        else:
            e.extend(f.pop())
    return e


async def get_matrix(url: str) -> list[int]:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                square_str = await response.content.read()
    except Exception as e:
        print(e)

    square_list = square_str_to_square_list(square_str.decode("utf-8"))
    line_list = square_list_to_line_list(square_list)

    return line_list


if __name__ == "__main__":
    SOURCE_URL = input("Введите url: ")
    if SOURCE_URL == "":
        SOURCE_URL = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
        print("Вы не ввели url матрицы. Будет применена тестовая матрица.")
    # line_list = asyncio.run(get_matrix(SOURCE_URL))
    # применение команды asyncio.run() дает ошибку RuntimeError: Event loop is closed
    line_list = asyncio.get_event_loop().run_until_complete(get_matrix(SOURCE_URL))
    print(line_list)
