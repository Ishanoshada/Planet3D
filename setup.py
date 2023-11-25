from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Planet3D",
    version="0.2.0",
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku@gmail.com",
    description="A 3D representation of the solar system using Pygame and OpenGL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/Planet3D",
    packages=find_packages(),
    install_requires=[
        "pygame",
        "PyOpenGL",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
