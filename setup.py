
import os
from setuptools import setup, find_packages

setup(
    name="betdaq_py",
    version="0.0.1",
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Betdaq API Python wrapper",
    url="https://github.com/rozzac90/betdaq_py",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
