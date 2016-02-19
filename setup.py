import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='jserr',
    version=open('VERSION').read(),
    license='BSD 2',
    packages = find_packages() + ['jserr'],
    package_dir={'jserr': 'jserr'},
    package_data={'jserr': ['regexes.yaml']},
    long_description=open('README.md').read(),
    install_requires=[
        'PyYAML',
    ],
)
