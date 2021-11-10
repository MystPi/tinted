import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tinted",
    version="1.0.0",
    description="Give your print output the tint it deserves!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MystPi/tinted",
    author="MystPi",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["tinted"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "tinted=tinted.__main__:main",
        ]
    },
)