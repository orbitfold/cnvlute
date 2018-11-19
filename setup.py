from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='cnvlute',
    version='0.0.1',
    description='A toolkit for combining and manipulating audio files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/orbitfold/cnvlute',
    author='Vytautas Jancauskas',
    author_email='unaudio@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['numpy', 'scipy', 'sklearn', 'sounddevice'],
    scripts=['bin/cnvlute']
)
