try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This project provides a database schema for sports data and the machine learning tooling available to use the database to predict future games.',
    'author': 'Douglas Melvin',
    'url': 'github.com/duggym122/grays_sports_almanac',
    'download_url': 'https://github.com/duggym122/grays_sports_almanac/archive/v0.0.1.zip',
    'version': '0.0.1',
    'install_requires': ['nose','psycopg2~=2.6.2','https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp27-none-linux_x86_64.whl'],
    'packages': ['grays_sports_almanac'],
    'scripts': [],
    'name': 'grays_sports_almanac'
}

setup(**config)