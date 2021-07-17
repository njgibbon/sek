from setuptools import setup, find_packages

setup(
    name="sek",
    version="0.0.1",
    author="Nick Gibbon",
    packages=find_packages(),
)

setup(
    name='sek',
    entry_points={
        'console_scripts': [
            'sek = sek:main',
        ],
    }
)
