from setuptools import setup, find_packages

setup(
    name='pushgp',
    version='0.1.0',
    description='Use genetic programming, implemented with Push, for machine learning.',
    long_description=open('README.rst').read(),
    author='Saul Shanabrook',
    author_email='s.shanabrook@gmail.com',
    url='https://github.com/saulshanabrook/pushgp.py',
    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=[
        'numpy',
        'scipy',
        #'Matplotlib',
        #'jinja2',
        #'pyzmq',
        'scikit-learn==0.15-git',
    ],
    dependency_links=[
        'https://github.com/scikit-learn/scikit-learn/tarball/master#egg=gearman-0.15-git'
    ],
    license="BSD",
    zip_safe=False,
    keywords='pushgp.py',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
