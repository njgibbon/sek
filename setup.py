from setuptools import setup

setup(
    name='sek',
    version='0.0.6',
    author="Nick Gibbon",
    packages=["src"],
    entry_points={
        'console_scripts': [
            'sek = src.sek:main',
        ],
    }
)
