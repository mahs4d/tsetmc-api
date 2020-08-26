from setuptools import setup

setup(
    name='tsetmc-api',
    version='2.1.0',
    package_dir={'': 'lib'},
    packages=['tsetmc_api', 'tsetmc_api.core'],
    install_requires=['requests>=2', 'beautifulsoup4>=4', 'lxml>=4', 'python-dateutil>=2', 'jdatetime>=3', 'schedule>=0'],
    url='https://github.com/mahs4d/tsetmc-api',
    license='MIT',
    author='Mahdi Sadeghi',
    author_email='mail2mahsad@gmail.com',
    description='getting data from tehran stock exchange'
)
