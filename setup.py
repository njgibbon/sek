from setuptools import setup
from setuptools import find_packages

setup(
    name='sek',
    description='Live Cloud Resource Security Configuration Scanning.',
    long_description='Live Cloud Resource Security Configuration Scanning.',
    url='https://github.com/njgibbon/sek',
    version='0.0.14',
    python_requires=">=3.7",
    author="Nick Gibbon",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sek = sek.main:main',
        ],
    }
)
