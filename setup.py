import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='pushgp',
    version='0.1.0',
    description='Use genetic programming, implemented with Push, for machine learning.',
    long_description=readme,
    author='Saul Shanabrook',
    author_email='s.shanabrook@gmail.com',
    url='https://github.com/saulshanabrook/pushgp.py',
    packages=[
        'pushgp',
    ],
    package_dir={'pushgp': 'pushgp'},
    install_requires=[
        'numpy',
        'scipy',
        'Matplotlib',
        'inspyred',
        'jinja2',
        'pyzmq',
        'scikit-learn',
        'future',
    ],
    license="BSD",
    zip_safe=False,
    keywords='pushgp.py',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
