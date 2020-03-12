import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloopencv", # Replace with your own username
    version="0.0.1",
    author="Lucas Martins de Castro",
    author_email="lucas.martins.c03@gmail.com",
    description="Um primeiro programe opencv hello world",
    url="http://www.lucmcast.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)