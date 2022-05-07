import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='faktura-qr-code-reader',
    version='0.0.1',
    author="Erik Holmström",
    author_email="erik.holmstrom93@gmail.com",
    description="Functionality for reading qr codes on Swedish invoices",
    long_description=long_description,
    url="https://github.com/ErikHolmstrom/qr-code-reader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",

)