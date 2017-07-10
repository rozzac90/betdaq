
from setuptools import setup, find_packages
from betdaq import __version__

setup(
    name="betdaq",
    version=__version__,
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Betdaq API Python wrapper",
    url="https://github.com/rozzac90/betdaq_py",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open('README.rst').read(),
    tests_require=['pytest'],
)
