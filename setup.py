from setuptools import setup

setup(
    name='tsetmc-api',
    version='0.2.1',
    package_dir={'': 'lib'},
    packages=['tsetmc_api'],
    install_requires=['requests>=2', 'beautifulsoup4>=4'],
    url='https://github.com/mahs4d/tsetmc-api',
    license='MIT',
    author='Mahdi Sadeghi',
    author_email='mail2mahsad@gmail.com',
    description='getting data from tehran stock exchange'
)
