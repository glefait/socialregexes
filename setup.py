#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='socialregexes',
    version=0.1 ,
    url='https://github.com/glefait/socialregexes',
    description='Identify social network user account from url',
    long_description=open('README.rst').read(),
    author='guillem lefait',
    author_email='guillem.lefait@gmail.com',
    license='MIT',
    keywords='social-network user account spyder crawler parser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': ['socialregexes = socialregexes:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)