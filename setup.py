import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-vanderbeck", # Replace with your own username
    version="0.0.1",
    author="Lindsay Vanderbeck",
    author_email="lindsay.vanderbeck@live.ca",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vanderbeck/example_pkg.git",
    packages=setuptools.find_packages(),
    install_requires=[
          'regex'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.5',
    # entry_points = {
    #     'console_scripts' : ['example_pkg = myscript.myscript:main']
    # },
)
