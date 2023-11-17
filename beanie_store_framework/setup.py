from setuptools import setup, find_packages

setup(
    name='Beanie_framework',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beanie'
    ],
    entry_points={
        'console_scripts': [
            'item-cli = Beanie_framework.main:main_function',
        ],
    },
)
