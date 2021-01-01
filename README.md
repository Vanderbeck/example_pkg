# A dpkg tutorial

## Introduction
The goal of this project is to create a dpkg installable binary which contains
python code. The python code will be multiple scripts and reference at least one
non-standard library which is usually installed via pip.

## Python packaging
**links**
https://docs.python.org/3/distributing/index.html#distributing-index
https://packaging.python.org/tutorials/packaging-projects/
https://packaging.python.org/tutorials/packaging-projects/#packaging-your-project

**Commands I Learned**
```
python3 -m pip install --user --upgrade setuptools wheel  # For install
python3 setup.py sdist bdist_wheel                        # To compile
pip install example_pkg_vanderbeck-0.0.1-py3-none-any.whl # To install locally
```

##Deb Packaging
https://stackoverflow.com/questions/7110604/is-there-a-standard-way-to-create-debian-packages-for-distributing-python-progra
