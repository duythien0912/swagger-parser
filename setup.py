#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from pip.req import parse_requirements

# try: # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError: # for pip <= 9.0.3
#     from pip.req import parse_requirements

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = [str(i.req) for i in parse_requirements('requirements.txt'
                                                      # , session=False
#                                                       )]
# test_requirements = [str(i.req) for i in parse_requirements('requirements_dev.txt'
                                                            #, session=False
#                                                            )]

install_reqs = parse_requirements('requirements.txt')
requirements = install_reqs
install_reqs_test = parse_requirements('requirements_dev.txt')
test_requirements = install_reqs_test


setup(
    name='swagger_parser',
    version='1.0.1',
    description="Swagger parser giving useful informations about your swagger files",
    long_description=readme + '\n\n' + history,
    author="Cyprien Guillemot",
    author_email='cyprien.guillemot@gmail.com',
    url='https://github.com/Trax-air/swagger-parser',
    packages=[
        'swagger_parser',
    ],
    package_dir={'swagger_parser':
                 'swagger_parser'},
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='swagger, parser, API, REST, swagger-parser',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
