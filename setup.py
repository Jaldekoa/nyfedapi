from setuptools import setup
from pathlib import Path

VERSION = "0.0.1"
THIS_PATH = Path(__file__).parent
DESCRIPTION = "A Python wrapper to easily retrieve data from the Federal Reserve Bank of New York (FRBoNY) official API in pandas format."
LONG_DESCRIPTION = (THIS_PATH / "README.md").read_text(encoding="utf-8")


setup(
    name="nyfedapi",
    version=VERSION,
    url="https://github.com/Jaldekoa/nyfedapi",
    author="Jon Aldekoa",
    author_email="jaldekoa@gmail.com",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=["nyfedapi", "nyfedapi.ambs", "nyfedapi.fxs", "nyfedapi.guidesheets", "nyfedapi.marketshare", "nyfedapi.pd", "nyfedapi.rates", "nyfedapi.rp", "nyfedapi.seclending", "nyfedapi.soma", "nyfedapi.tsy"],
    test_suite='nyfedapi.tests',
    platforms=["Any"],
    install_requires=["setuptools>=68.2", "pandas>=2.0.0", "requests>=2.23.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
    ]
)