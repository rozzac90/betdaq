import re
from setuptools import setup, find_packages


with open('betdaq/__init__.py', 'r') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE
    ).group(1)

setup(
    name="betdaq",
    version=version,
    author="Rory Cole",
    author_email="rory.cole1990@gmail.com",
    description="Betdaq API Python wrapper",
    url="https://github.com/rozzac90/betdaq_py",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    long_description=open('README.md').read(),
    tests_require=['pytest'],
)
