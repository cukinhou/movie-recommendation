from distutils.core import setup

setup(
    name='MovieRecNI',
    version='1.0.0',
    author='J. Nistal Hurle',
    author_email='j.nistalhurle@gmail.com',
    packages=['movierec', 'tests'],
    scripts=['movierec/main.py'],
    url='http://pypi.python.org/pypi/MovieRec/',
    license='LICENSE.txt',
    description='Movie recommendation.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy == 1.11.0",
        "pandas == 0.19.2",
    ],
)
