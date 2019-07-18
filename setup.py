from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MarketWatchBI',
    version='0.0.1',
    description='Web scrapper to excel for Reserve Bank of India',
    long_description=readme,
    author="Ervin Canigur",
    url='https://github.com/ervincanigur/MarketWatchBI',
    license=license,
    packages=find_packages()
)
