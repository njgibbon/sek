from setuptools import setup
from setuptools import find_packages

setup(
    name='sek',
    version='0.0.13',
    author="Nick Gibbon",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sek = sek.main:main',
        ],
    }
)
