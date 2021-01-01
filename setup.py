from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
lib = path.join(here, "lib")

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tsetmc-api",
    version="4.3.0",
    python_requires=">=3.7",
    install_requires=[
        "beautifulsoup4",
        "certifi",
        "chardet",
        "idna",
        "jdatetime",
        "lxml",
        "python-dateutil",
        "requests",
        "schedule",
        "six",
        "soupsieve",
        "urllib3",
    ],
    extras_require={
        "dev": [
            "appdirs",
            "attrs",
            "black",
            "bleach",
            "cached-property",
            "cerberus",
            "certifi",
            "cffi",
            "chardet",
            "click",
            "colorama",
            "cryptography",
            "distlib",
            "docutils",
            "idna",
            "jeepney",
            "keyring",
            "orderedmultidict",
            "packaging",
            "pathspec",
            "pep517",
            "pip-shims",
            "pipenv-setup",
            "pipfile",
            "pkginfo",
            "plette[validation]",
            "pycparser",
            "pygments",
            "pyparsing",
            "python-dateutil",
            "readme-renderer",
            "regex",
            "requests",
            "requests-toolbelt",
            "requirementslib",
            "rfc3986",
            "secretstorage",
            "six",
            "toml",
            "tomlkit",
            "tqdm",
            "twine",
            "typed-ast",
            "urllib3",
            "vistir",
            "webencodings",
            "wheel",
        ]
    },
    package_dir={"": "lib"},
    packages=find_packages(where=lib, exclude=["scripts"]),
    entry_points={
        "console_scripts": ["tsetmc-loader = tsetmc_api.bin.tsetmc_loader:main"]
    },
    url="https://github.com/mahs4d/tsetmc-api",
    license="MIT",
    author="Mahdi Sadeghi",
    author_email="mail2mahsad@gmail.com",
    description="getting data from tehran stock exchange",
)
