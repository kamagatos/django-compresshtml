# Copyright 2012 django-compresshtml authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from setuptools import setup, find_packages

README = open('README.md').read()

setup(
		name='django-compresshtml',
		version='0.1.2',
		description='HTML compressor for django',
		packages=find_packages(),
		include_package_data=True,
		license='BSD License',
		long_description=README,
		author='Kamagatos',
		author_email='kamagatos@gmail.com',
	)
