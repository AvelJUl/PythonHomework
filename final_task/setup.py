import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='pycalc',
    version='1.0.0',
    description='Console calculator',
    packages=find_packages(),
    long_description=read('README.md'),
    entry_points={
        'console_scripts': [
            'pycalc=console.__main__:main'
        ],
    },
)
