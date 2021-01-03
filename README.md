# A dpkg tutorial

## Introduction
The goal of this project is to create a dpkg installable binary which contains
python code. The python code will be multiple scripts and reference at least one
non-standard library which is usually installed via pip.

## Python packaging
**links**

[Intro to python packaging](https://docs.python.org/3/distributing/index.html#distributing-index)

[The meat of the process](https://packaging.python.org/tutorials/packaging-projects/)

**Commands I Learned**
```
python3 -m pip install --user --upgrade setuptools wheel  # For install
python3 setup.py sdist bdist_wheel                        # To compile
pip install example_pkg_vanderbeck-0.0.1-py3-none-any.whl # To install locally
```

## Deb Packaging
**Links**

[The easy setuptools method](https://stackoverflow.com/questions/17401381/debianzing-a-python-program-to-get-a-deb)

[More involved with debhelper and pybuild](https://www.geekyhacker.com/2016/05/19/how-to-create-debian-package-for-python-script/)

[Great dpkg creation article](https://www.devdungeon.com/content/debian-package-tutorial-dpkgdeb#toc-2)

**Debian wesite**

[Python](https://wiki.debian.org/Python)

[Packaging policy](https://wiki.debian.org/Python/LibraryStyleGuide?action=show&redirect=Python%2FPackaging#Style_Guide_for_Packaging_Python_Libraries)

**Commands I learned**
```
sudo apt install python3-stdeb fakeroot python3-all         # To install
python3 setup.py --command-packages=stdeb.command bdist_deb # To compile
dpkg -i python3-example-pkg-vanderbeck_0.0.1-1_all.deb      # To intsall
sudo apt install ./name.deb                                 # To install with deps
```


## Future Reading

https://github.com/urban48/debpackager
