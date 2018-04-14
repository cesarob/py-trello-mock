from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='trellomock',
    description='An in memory py-trello mock',
    packages=find_packages(exclude=('test')),
    install_requires=requirements
)
