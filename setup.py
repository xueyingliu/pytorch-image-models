""" Setup
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

exec(open('timm/version.py').read())
setup(
    name='timm',
    version=__version__,
    description='(Unofficial) PyTorch Image Models',
    long_description=long_description,
    url='https://github.com/rwightman/pytorch-image-models',
    author='Ross Wightman',
    author_email='hello@rwightman.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 3.6',
    ],

    # Note that this is a string of words separated by whitespace, not a list.
    keywords='pytorch pretrained models efficientnet mobilenetv3 mnasnet',
    packages=find_packages(exclude=['convert']),
    install_requires=['torch', 'torchvision'],
    python_requires='>=3.6',
)