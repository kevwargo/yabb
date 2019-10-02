from setuptools import setup, find_packages


setup(
    name='yabb',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'yabb = yabb:main'
        ]
    }
)
