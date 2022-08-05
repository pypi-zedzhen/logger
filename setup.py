from setuptools import setup, find_packages

setup(
    name='logger',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/pypi-zedzhen/logger',
    license='zlib/libpng License',
    license_files='LICENSE',
    author='Ярыкин Евгений',
    description='Логирование работы программы',
    install_requires=[
        'dill>=0.3.4',
    ],
    python_requires='>=3.8',
)
