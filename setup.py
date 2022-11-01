#! /usr/bin/env python3
#
#  Copyright 2022 Jinshun Zhu
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# yagt: Yet Another Geographic Toolkit
# Author: Jinshun Zhu, zhujinshun@pku.edu.cn
#

from io import open
from setuptools import setup, find_packages
from yagt import __version__

with open('README.rst', 'r') as f:
    LONG_DESCRIPTION = f.read()

LICENSE = "Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)"

setup(name='yagt',
      version=__version__,
      url='http://github.com/tirzhu/yagt/',
      license=LICENSE,
      author='Jinshun Zhu',
      author_email='tirzhu@gmail.com',
      description='Yet Another Geographic Toolkit',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/x-rst',
      packages=find_packages(),
      include_package_data=True,
      scripts=[
          'bin/yagt',
      ],
      install_requires=[
          'numpy>=1.11', 'scipy>=1.3.0', 'matplotlib>=2.2.2',
          'scikit-learn>=0.19.1', 'pytest>=3.5.1', 'pep8>=1.7.1',
          'pyyaml>=5.1.2', 'pandas>=0.24', "geptiff>=0.2.7"
      ],
      python_requires='>=3',
      platforms='any',
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent'
      ])
