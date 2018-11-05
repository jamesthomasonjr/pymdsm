from setuptools import setup
setup(
    name='pymdsm',
    decsription='A python markdown extension that converts ..content.. to <small>content</small>',
    version='0.0.1',
    url='https://github.com/jamesthomasonjr/pymdsm',
    author='James Thomason, Jr',
    author_email='james@jamesthomasonjr.com',
    license='MIT',
    py_modules=['pymdsm'],
    install_requires=['markdown>=2.5'],
)
