import setuptools

setuptools.setup(
    name='faktura-qr-code-reader',
    version='0.1',
    scripts=['QrCodeReader'],
    author="Erik Holmström",
    author_email="erik.holmstrom93@gmail.com",
    description="A package for reading qr codes on Swedish invoices",
    url="https://github.com/ErikHolmstrom/qr-code-reader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)