# -*- coding: utf-8 -*-
# Copyright 2012 Yoshihisa Tanaka
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from setuptools import find_packages, setup

name = 'recox'
version = '0.0.0'

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
changes = os.path.join(os.path.dirname(__file__), 'CHANGES.rst')
long_description = open(readme).read() + '\n\n' + open(changes).read()

install_requires=[
    'lxml'
]

classifiers = [
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: POSIX :: Linux',
    'Development Status :: 3 - Alpha'
]

setup(name=name,
      version=version,
      author='Yoshihisa Tanaka',
      author_email='yt.hisa@gmail.com',
      license='LICENSE',
      url='https://github.com/yosisa/recox',
      description='Software suite for tv recording in Japan',
      long_description=long_description,
      classifiers=classifiers,
      keywords=[],
      install_requires=install_requires,
      tests_require=install_requires+['pytest', 'pytest-pep8', 'mock'],
      packages=find_packages(exclude=['tests'])
)
