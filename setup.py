import os

from setuptools import setup


def get_directory_files(dir):
    listOfFile = os.listdir(dir)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dir, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_directory_files(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


data_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './lib/tsetmc_api/data')

setup(
    name='tsetmc-api',
    version='1.3.0',
    package_dir={'': 'lib'},
    packages=['tsetmc_api'],
    package_data={'tsetmc_api': get_directory_files(data_dir_path)},
    include_package_data=True,
    install_requires=['requests>=2', 'beautifulsoup4>=4', 'lxml>=4', 'python-dateutil>=2'],
    url='https://github.com/mahs4d/tsetmc-api',
    license='MIT',
    author='Mahdi Sadeghi',
    author_email='mail2mahsad@gmail.com',
    description='getting data from tehran stock exchange'
)
