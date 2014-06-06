#!/usr/bin/env python

from distutils.core import setup
from soar.version import format_version

setup(name='lib601',
      version=format_version(),
      description='6.01 Code Distribution',
      author='6.01 Staff',
      author_email='6.01-help@mit.edu',
      license='GPLv2',
      url='http://mit.edu/6.01/',
      packages = ['lib601','form','soar','soar.io','soar.graphics','soar.serial','soar.controls','soar.outputs'],
      package_data={'lib601': ['*.pyc'],'soar': ['media/*','worlds/*']},
      scripts=['lib601/CMax','soar/soar'],
     )
