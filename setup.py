from setuptools import find_packages, setup

with open("README.txt", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "asyncio>=3.4",
    "aiohttp>=3.8",
]

setup(
    name="square_to_list",
    version="0.0.1",
    author="Dimasuz",
    author_email="dimaskus@gmail.com",
    description="A package to convert str square matrix to list[int]",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/square-to-list/square-to-list.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: no",
    ],
)
