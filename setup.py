from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pymdsm',
    description='A python markdown extension that converts ..content.. to <small>content</small>',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.0.3',
    url='https://github.com/jamesthomasonjr/pymdsm',
    author='James Thomason, Jr',
    author_email='james@jamesthomasonjr.com',
    license='MIT',
    packages=['pymdsm'],
    install_requires=['markdown>=2.5'],
)
