import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="b3futurecontracts",
    version="0.0.1",
    author="Alvaro Figueiredo",
    author_email="alvaro.af@gmail.com",
    description="Rollover date of future contracts from the B3 exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvfig/b3futurecontracts",
    py_modules=['b3futurecontracts'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
