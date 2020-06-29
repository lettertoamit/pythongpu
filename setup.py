from setuptools import setup, find_packages

setup(
    name='randomquote',
    version='0.1',
    description='Get a random quote',
    url='https://github.com/lettertoamit/pythongpu',
    author='Amit sharma',
    author_email='lettertoamit@gmail.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:display_quote']
    )
)